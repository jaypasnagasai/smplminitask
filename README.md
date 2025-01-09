# LLLMotion Mini-Task: Extracting Pose Parameters of Left Knee

## AGENDA

To load a AMASS dataset of a particular motion and extract the left_knee angles.

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
- Render Duration: 3 s

### NPZ KEYS BREAKDOWN

1. `trans`: (360,3)
2. `gender`: Female [Scalar]
3. `mocap_framerate`: 120 [Scalar]
4. `betas`: (16)
5. `dmpls`: (360,8)
6. `poses`: (360,156)

