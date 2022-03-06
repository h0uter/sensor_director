# sensor_director
Package for calculating quaternions to point sensors at targets.

### Quickstart
```python

import sensor_director as sd

# calc the rotation necesary to look at a target from a source pose

source_pose = AgentPose(Position(x=5, y=5, z=5), Quaternion(w=0, i=0, j=0, k=0))

target_point = TargetPoint(Position(x=8, y=0, z=0))


rotation = sd.calc_rotation_to_look_at_target(source_pose, target_point)

```

reference [quaternions double check](https://quaternions.online/)


# Dev
It important to maintain the up direction while directing the sensor.
So we need to translate between two frames, not just two vectors

## Up Next

- [ ] write some tests for basic cases
- [ ] derive the view vetor from point and agent
- [ ] calculate the rotation between current pose and view vector
- [ ] vizualise the result