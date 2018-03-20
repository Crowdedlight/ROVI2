import numpy as np
from numpy.linalg import inv, norm
from numpy.random import randn
from math import pi

class KalmanFilter(object):

    def __init__(self, initial_state, dt, boxWidth, boxHeight, maxPredictions, velocityThresh, startDelay):
        self.x      = initial_state
        self.dt     = dt
        self.F      = np.array([[1,0,dt,0],[0,1,0,dt],[0,0,1,0],[0,0,0,1]])
        self.G      = np.array([[0.5*dt**2],[0.5*dt**2],[dt],[dt]])
        # self.G      = np.array([[0.5*dt**2,0],[0,0.5*dt**2],[dt,0],[0,dt]])
        self.H      = np.array([[1,0,0,0],[0,1,0,0]])

        self.P_min  = np.eye(4)
        self.P_plus = np.eye(4)

        self.x_hat_min  = self.x
        self.x_hat_plus = self.x

        self.boxWidth = boxWidth
        self.boxHeight = boxHeight

        # Members for detecting self-destruct condition
        self.maxPredictions = maxPredictions
        self.predictionCount = 0
        self.selfDestruct = False

        # Members for delaying drawing feature
        self.correctionCount = 0
        self.startDelay = startDelay
        self.valid = False

        self.velocityThreshold = velocityThresh

        # Error matrices from Agus lecture
        measurementNoise    = 0.1
        modelNoise          = 2
        self.Q      = np.eye(4)*modelNoise**2*dt
        self.R      = np.eye(2)*measurementNoise**2/dt

        # Error matrices from youtube
        # measurementNoise = 0.5
        # self.R      = np.eye(2)*measurementNoise**2/dt
        # self.Q      = np.array([[pow(dt,4)/4,    0,              pow(dt,3)/2,    0],
        #                         [0,              pow(dt,4)/4,    0,              pow(dt,3)/2],
        #                         [pow(dt,3)/2,    0,              dt**2,          0],
        #                         [0,              pow(dt,3)/2,    0,              dt**2]])*dt

    def update(self, y=None):
        # If there is no new measurement, then we can only make a prediction

        x, P = self.predict()
        x0 = self.x_hat_plus

        if type(y) != type(None):
            x, P = self.correct(y)
            self.predictionCount = 0
            self.correctionCount += 1

        else:
            # The prediction was the best we could do in this iteration, so x_hat_plus and P_plus
            # are assigned to the result from the prediction
            self.x_hat_plus = x
            self.P_plus = P
            self.predictionCount += 1

        angle = self.checkAngleDifference(x0,x)
        abs_vel = self.getAbsVelocity()

        if self.correctionCount > self.startDelay:
            self.valid = True

        if (self.predictionCount > self.maxPredictions) or (abs(angle) > pi/2) or \
                                    (self.valid and abs_vel < self.velocityThreshold):

            self.selfDestruct = True


        return x


    def predict(self):
        # For prediction we can only make a priori estimates
        # We need to increase the uncertainty in P
        self.P_min = self.F @ self.P_plus @ self.F.T + self.Q

        # Then we need to make our state prediction based on our model
        # a = randn()*
        self.x_hat_min = self.F @ self.x_hat_plus# + self.G * a

        # If this is all we do in this iteration then we need to update xhat_plus and P_plus as well
        # with our prediction estimates from this function, because they are used at the beginning of each
        # iteration

        # self.x_hat_plus = self.x_hat_min
        # self.P_plus     = self.P_min

        # This can also be taken care of in the update function

        return self.x_hat_min, self.P_min

    def correct(self, y):
        # Use long formula from book to calculate the kalman gain from P_min instead of P_plus
        # This is necessary if P_plus is changed in the predict function
        self.K = self.P_min@self.H.T@inv(self.H@self.P_min@self.H.T + self.R)

        # P_plus has to be the P_plus from the previous iteration; it must not be calculated in the
        # predict function
        # self.K          = self.P_plus @ self.H.T @ inv(self.R)

        self.x_hat_plus = self.x_hat_min + self.K @ (y - self.H @ self.x_hat_min)
        self.P_plus     = (np.eye(4) - self.K @ self.H) @ self.P_min

        return self.x_hat_plus, self.P_plus

    def getState(self):
        return self.x_hat_plus

    def getPosition(self):
        return np.array([self.x_hat_plus[0,0], self.x_hat_plus[1,0]])

    def getAbsVelocity(self):
        v = np.array([self.x_hat_plus[2, 0], self.x_hat_plus[3, 0]])
        v = norm(v)
        return v

    def getSize(self):
        return self.boxWidth, self.boxHeight

    def selfDestructing(self):
        return self.selfDestruct

    def validFilter(self):
        return self.valid

    def checkAngleDifference(self,state1,state2):
        # Compare the vector of the new velocity to the vector between
        # positions of the previous and current iteration
        # if the angle is too great, then the change in direction is too sudden

        posPrev = np.array([state1[0,0],state1[1,0]])
        posCurr = np.array([state2[0,0],state2[1,0]])
        velCurr = np.array([state2[2,0],state2[3,0]])

        vec1 = posCurr - posPrev
        vec2 = velCurr

        def unit_vector(vector):
            """ Returns the unit vector of the vector.  """
            return vector / np.linalg.norm(vector)

        def angle_between(v1, v2):
            """ Returns the angle in radians between vectors 'v1' and 'v2'::

                    >>> angle_between((1, 0, 0), (0, 1, 0))
                    1.5707963267948966
                    >>> angle_between((1, 0, 0), (1, 0, 0))
                    0.0
                    >>> angle_between((1, 0, 0), (-1, 0, 0))
                    3.141592653589793
            """
            v1_u = unit_vector(v1)
            v2_u = unit_vector(v2)
            return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))

        return angle_between(vec1,vec2)