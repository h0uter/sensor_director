import vedo
from collections import namedtuple

vedo.settings.allowInteraction = True


def draw_agent(agent):

    actors = list()

    axis = vedo.Point((agent.x, agent.y, agent.z), r=20, c='r')
    actors.append(axis)

    vedo.show(actors, axes=3)

    
def main():
    AgentPose = namedtuple('AgentPose', ['x', 'y', 'z', "w", "i", "j", "k"])
    agent_pose = AgentPose(x=0, y=0, z=0, w=0, i=0, j=0, k=0)

    draw_agent(agent_pose)

if __name__ == "__main__":
    main()
