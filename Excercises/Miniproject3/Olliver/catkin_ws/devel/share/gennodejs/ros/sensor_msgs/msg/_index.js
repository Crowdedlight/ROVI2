
"use strict";

let JoyFeedback = require('./JoyFeedback.js');
let LaserScan = require('./LaserScan.js');
let Joy = require('./Joy.js');
let CameraInfo = require('./CameraInfo.js');
let CompressedImage = require('./CompressedImage.js');
let MultiDOFJointState = require('./MultiDOFJointState.js');
let Image = require('./Image.js');
let Range = require('./Range.js');
let MultiEchoLaserScan = require('./MultiEchoLaserScan.js');
let Temperature = require('./Temperature.js');
let BatteryState = require('./BatteryState.js');
let JointState = require('./JointState.js');
let RelativeHumidity = require('./RelativeHumidity.js');
let MagneticField = require('./MagneticField.js');
let Illuminance = require('./Illuminance.js');
let RegionOfInterest = require('./RegionOfInterest.js');
let PointCloud2 = require('./PointCloud2.js');
let NavSatStatus = require('./NavSatStatus.js');
let TimeReference = require('./TimeReference.js');
let ChannelFloat32 = require('./ChannelFloat32.js');
let Imu = require('./Imu.js');
let NavSatFix = require('./NavSatFix.js');
let JoyFeedbackArray = require('./JoyFeedbackArray.js');
let PointCloud = require('./PointCloud.js');
let LaserEcho = require('./LaserEcho.js');
let PointField = require('./PointField.js');
let FluidPressure = require('./FluidPressure.js');

module.exports = {
  JoyFeedback: JoyFeedback,
  LaserScan: LaserScan,
  Joy: Joy,
  CameraInfo: CameraInfo,
  CompressedImage: CompressedImage,
  MultiDOFJointState: MultiDOFJointState,
  Image: Image,
  Range: Range,
  MultiEchoLaserScan: MultiEchoLaserScan,
  Temperature: Temperature,
  BatteryState: BatteryState,
  JointState: JointState,
  RelativeHumidity: RelativeHumidity,
  MagneticField: MagneticField,
  Illuminance: Illuminance,
  RegionOfInterest: RegionOfInterest,
  PointCloud2: PointCloud2,
  NavSatStatus: NavSatStatus,
  TimeReference: TimeReference,
  ChannelFloat32: ChannelFloat32,
  Imu: Imu,
  NavSatFix: NavSatFix,
  JoyFeedbackArray: JoyFeedbackArray,
  PointCloud: PointCloud,
  LaserEcho: LaserEcho,
  PointField: PointField,
  FluidPressure: FluidPressure,
};
