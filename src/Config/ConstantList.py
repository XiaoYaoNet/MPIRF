# coding=UTF-8

'''
ConstantList.py:The global constants of the MPIRF are defined in this module.
'''

# The global constants used by MDFReader
SYSMTRMEASDATA='/measurement/data'

MEASSIGNALDATA='/measurement/data'

ISBACKGROUNDFRAME='/measurement/isBackgroundFrame'

NUMSAMPLINGPOINTS='/acquisition/receiver/numSamplingPoints'

CALIBRATIONSIZE='/calibration/size'

# The global constants used by DataBase
MAGNETICPARTICL  =  'MagneticParticle'
DIAMETER         =  'Diameter'
SATURATIONMAG    =  'SaturationMag'
TEMPERATURE      =  'Temperature'

SELECTIONFIELD   =  'SelectionField'
XGRADIENT        =  'Xgradient'
YGRADIENT        =  'Ygradient'
ZGRADIENT        =  'Zgradient'

DRIVEFIELD       =  'DriveField'
XDIRECTIOND      =  'Xdirection'
YDIRECTIOND      =  'Ydirection'
ZDIRECTIOND      =  'Zdirection'
REPEATTIME       =  'RepeatTime'
WAVEFORMD        =  'Waveform'

FOCUSFIELD       =  'FocusField'
XDIRECTIONF      =  'Xdirection'
YDIRECTIONF      =  'Ydirection'
ZDIRECTIONF      =  'Zdirection'
WAVEFORMF        =  'Waveform'

SAMPLE           =  'Sample'
TOPOLOGY         =  'Topology'
FREQUENCY        =  'Frequency'
SAMNUMBER        =  'Number'
BEGINTIME        =  'BeginTime'
SENSITIVITY      =  'Sensitivity'

MEASUREMENT      =  'Measurement'
TYPE             =  'Type'
BGFLAG           =  'BgFlag'
MEASIGNAL        =  'MeaSignal'
AUXSIGNAL        =  'AuxSignal'
MEANUMBER           =  'Number'

SINE             =  1
TRIANGLE         =  2
FFP              =  1
FFL              =  2
SYSTEMMATRIX     =  1
FFAVELOCITY      =  2

# DataBase and Xpace Extended
EXTENDED='Extended'
RFFP='Rffp'
FFP='Ffp'
STEP='Step'

# The global constants used by Phantom
PI = 3.1416
KB = 1.3806488e-23
TDT = 273.15
U0 = 4.0 * PI * 1e-7