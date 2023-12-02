import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Forward Kinematics
def forward_kinematics(thetas):
    for i in range(1, joints.shape[0]):
        joints[i] = joints[i-1] + np.array([lengths[i-1]*np.cos(np.sum(thetas[:i]))*np.cos(thetas[-1]), lengths[i-1]*np.cos(np.sum(thetas[:i]))*np.sin(thetas[-1]), lengths[i-1]*np.sin(np.sum(thetas[:i]))])
    
# Inverse Kinematics
def inverse_kinematics(coordinates, phi):
    thetas[-1] = np.arctan2(coordinates[1], coordinates[0])
    theta4_phi = np.array([np.cos(phi)*np.cos(thetas[-1]), np.cos(phi)*np.sin(thetas[-1]), np.sin(phi)])
    w = coordinates - lengths[2]*theta4_phi
    thetas[1] = np.arccos((np.sum(w**2) - np.sum(lengths[-2:]**2))/(2*np.prod(lengths[-2:])))
    x2 = np.sqrt(np.sum(w[:2]**2))
    c1 = (lengths[0] + lengths[1]*np.cos(thetas[1]))*x2 + lengths[1]*np.sin(thetas[1])*w[2]
    s1 = (lengths[0] + lengths[1]*np.cos(thetas[1]))*w[2] + lengths[1]*np.sin(thetas[1])*x2

    thetas[0] = np.arctan2(s1, c1)

    thetas[2] = phi - thetas[0] - thetas[1]

# Initailize required arrays and variables
lengths = np.array([2.5, 2.0, 1.5])
thetas = np.array([0.0, 0.0, 0.0, 0.0])
joints = np.zeros(shape=(4, 3))
step_size, space_limit = 0.01, 6.0

# Initialize using given conditions
initial = np.array(list(map(int, input("Enter initial coordinates: ").split())))
target = np.array(list(map(int, input("Enter target coordinates: ").split())))
phi = int(input("Angle of picking: "))*np.pi/180

# Adjustments according to initial conditions
inverse_kinematics(initial, phi)
thetas = np.array([0.0, 90.0, 180.0, 90.0])
forward_kinematics(thetas)

print(thetas)

fig = plt.figure(figsize=(8, 8))

ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(-space_limit, space_limit)
ax.set_ylim(-space_limit, space_limit)
ax.set_zlim(-space_limit, space_limit)

# '''
def init():
    for i in range(joints.shape[0]-1):
        ax.plot([joints[i,0], joints[i+1,0]], [joints[i,1], joints[i+1,1]], [joints[i,2], joints[i+1,2]], 'b-', lw=2)
    
    for i in range(joints.shape[0]-1):
        ax.scatter(joints[i,0], joints[i,1], joints[i,2], c='b', marker='o', label=f'Joint {i}')
    
    ax.scatter(target[0], target[1], target[2], c='k', marker='x', label='Target Coordinates')
    
    ax.legend()
    return ax

def animate(i):
    global thetas

    dtarget = step_size*(target - joints[-1])

    inverse_kinematics(joints[-1] + dtarget, phi)
    forward_kinematics(thetas)

    ax.cla()
    ax.set_xlim(-space_limit, space_limit)
    ax.set_ylim(-space_limit, space_limit)
    ax.set_zlim(-space_limit, space_limit)
    init()

# ani = FuncAnimation(fig, animate, init_func=init, frames=200, interval=50)

# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')
# ax.set_title('3R Manipulator Animation in 3D')
# ax.grid()

init()
plt.show()

# '''
