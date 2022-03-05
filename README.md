# sensor_director

### Quickstart
```python

import sensor_director as sd

# calc the rotation necesary to look at a target from a source pose

source_pose = AgentPose(Position(x=5, y=5, z=5), Quaternion(w=0, i=0, j=0, k=0))

target_point = TargetPoint(Position(x=8, y=0, z=0))


rotation = sd.calc_rotation_to_look_at_target(source_pose, target_point)

```

reference [quaternions double check](https://quaternions.online/)