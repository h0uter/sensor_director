import vedo

vedo.settings.allowInteraction = True


class Position:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    @property
    def vec(self):
        return (self.x, self.y, self.z)


class Quaternion:
    def __init__(self, w, i, j, k):
        self.w = w
        self.i = i
        self.j = j
        self.k = k

    @property
    def vec(self):
        return (self.w, self.i, self.j, self.k)


class AgentPose:
    def __init__(self, pos: Position, quat: Quaternion) -> None:
        self.pos = pos
        self.quat = quat


class TargetPoint:
    def __init__(self, pos: Position) -> None:
        self.pos = pos


def main():

    agent_pose = AgentPose(Position(x=5, y=5, z=5), Quaternion(w=0, i=0, j=0, k=0))

    target_point = TargetPoint(Position(x=8, y=0, z=0))

    draw_scene(agent_pose, target_point)


def draw_scene(agent, target):

    actors = list()

    """Take care of the agent pose"""
    arrow_len = 1
    start_point = (
        agent.pos.x - arrow_len,
        agent.pos.y - arrow_len,
        agent.pos.z - arrow_len,
    )

    agent_actor = vedo.Arrow(start_point, agent.pos.vec, c="r")

    actors.append(agent_actor)

    """"Take care of the target point"""
    target_actor = vedo.Point(target.pos.vec)
    actors.append(target_actor)

    """"viz the required rotation"""
    # center = agent.pos.vec
    center = (0,0,0)
    arc_actor = vedo.Arc(center, agent.pos.vec, target.pos.vec, c="b")
    actors.append(arc_actor)

    ax_range = (0, 10)

    axs = vedo.Axes(
        xrange=ax_range, yrange=ax_range, zrange=ax_range, htitle="Sensor Director"
    )

    vedo.show(actors, axes=axs)


if __name__ == "__main__":
    main()
