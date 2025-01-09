# LLLMotion Mini-Task: Extracting Pose Parameters of Left Knee

## OBJECTIVE

To load a AMASS dataset of a particular motion and extract the left_knee angles from the `pose` key.

## MASTER DATASET
The dataset the motion data has been extracted from 

- Dataset: [ACCAD](https://accad.osu.edu/research/motion-lab/mocap-system-and-data)
- Subjects: 20
- Motions: 252
- Video: 26.74 min

## EXAMPLE MOTION
The motion used to extract the left knee

- File Name: [A1 - Stand_poses.npz](stand.npz)
- Modified Name: [stand.npz](stand.npz)
- Gender: Female
- Frame Rate: 120 fps
- Video Duration: 3 s
- Total # of Frames: 360
- Type: SMPL-H

### KEYS BREAKDOWN

1. `trans`: (360,3) [The global translation (position) of the subject in 3D space for each frame of the motion sequence.]
    - 360: Total # Of Frames 
    - 3: Total # of Vector Components (x,y,z)
  
2. `gender`: Female [Scalar]

3. `mocap_framerate`: 120 [Scalar]

4. `betas`: (16) [The shape parameters of the SMPL. They encode the body shape in a low-dimensional space.]

5. `dmpls`: (360,8) [They encode soft tissue deformation effects during motion.]
    - 360: Total # Of Frames
    - 8: Number of dynamic parameters encoding soft tissue dynamics.

6. `poses`: (360,156) [They represent the orientation of the body joints in axis-angle format. They are measured in radians]
    - 360: Total # Of Frames
    - 156: 52 (Total # of Joints in SMPL-H Dataset) x 3 (Total # of Vector Components)

## IDENTIFYING LEFT KNEE

According to the [Meshcapade Wiki](https://github.com/Meshcapade/wiki/blob/main/wiki/SMPL.md), here is the legend of the SMPL-H skeleton dataset,
```
     0: 'pelvis',
     1: 'left_hip',
     2: 'right_hip',
     3: 'spine1',
     4: 'left_knee',
     5: 'right_knee',
     6: 'spine2',
     7: 'left_ankle',
     8: 'right_ankle',
     9: 'spine3',
    10: 'left_foot',
    11: 'right_foot',
    12: 'neck',
    13: 'left_collar',
    14: 'right_collar',
    15: 'head',
    16: 'left_shoulder',
    17: 'right_shoulder',
    18: 'left_elbow',
    19: 'right_elbow',
    20: 'left_wrist',
    21: 'right_wrist',
    22: 'left_index1',
    23: 'left_index2',
    24: 'left_index3',
    25: 'left_middle1',
    26: 'left_middle2',
    27: 'left_middle3',
    28: 'left_pinky1',
    29: 'left_pinky2',
    30: 'left_pinky3',
    31: 'left_ring1',
    32: 'left_ring2',
    33: 'left_ring3',
    34: 'left_thumb1',
    35: 'left_thumb2',
    36: 'left_thumb3',
    37: 'right_index1',
    38: 'right_index2',
    39: 'right_index3',
    40: 'right_middle1',
    41: 'right_middle2',
    42: 'right_middle3',
    43: 'right_pinky1',
    44: 'right_pinky2',
    45: 'right_pinky3',
    46: 'right_ring1',
    47: 'right_ring2',
    48: 'right_ring3',
    49: 'right_thumb1',
    50: 'right_thumb2',
    51: 'right_thumb3'
```
Left Knee is `[4]`. Hence we have to extract the `poses` parameters from row 12-14.

## IMPLEMENTATION

1. Install requirements.txt for required libraries
2. Run [main.py](main.py) to load [stand.npz](stand.npz)
3. Run [extract.py](extract.py) to create [leftknee.npz](stand.npz)
4. Run [main.py](main.py) to load [leftknee.npz](leftknee.npz)

## CONCLUSION

This is my first time completing a task for this project and documenting the process in GitHub. Any feedback would be appreciated. Thank You!





