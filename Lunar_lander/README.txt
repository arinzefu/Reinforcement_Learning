This was performed in google colab because there was an error installing box2d with pycharm.
This was inspired by huggingface reinforcement learning tutorial. I experienced an error pushing it to huggingface hub and couldnt resolve it.
NameError                                 Traceback (most recent call last)
<ipython-input-55-c2dbcf1e62cd> in <cell line: 30>()
     28 
     29 # method save, evaluate, generate a model card and record a replay video of your agent before pushing the repo to the hub
---> 30 package_to_hub(model=model, 
     31                model_name=model_name,
     32                model_architecture=model_architecture,

9 frames
/usr/local/lib/python3.9/dist-packages/gym/envs/classic_control/rendering.py in enable(self)

NameError: name 'glPushMatrix' is not defined

The game LunarLander is from https://www.gymlibrary.dev/environments/box2d/lunar_lander/ where you can see the documentation in full,
I will paste some of it from there here

Description
This environment is a classic rocket trajectory optimization problem. According to Pontryagin’s maximum principle, it is optimal to fire the engine at full throttle or turn it off. This is the reason why this environment has discrete actions: engine on or off.

There are two environment versions: discrete or continuous. The landing pad is always at coordinates (0,0). The coordinates are the first two numbers in the state vector. Landing outside of the landing pad is possible. Fuel is infinite, so an agent can learn to fly and then land on its first attempt.

To see a heuristic landing, run:

python gym/envs/box2d/lunar_lander.py
Action Space
There are four discrete actions available: do nothing, fire left orientation engine, fire main engine, fire right orientation engine.

Observation Space
The state is an 8-dimensional vector: the coordinates of the lander in x & y, its linear velocities in x & y, its angle, its angular velocity, and two booleans that represent whether each leg is in contact with the ground or not.

Rewards
Reward for moving from the top of the screen to the landing pad and coming to rest is about 100-140 points. If the lander moves away from the landing pad, it loses reward. If the lander crashes, it receives an additional -100 points. If it comes to rest, it receives an additional +100 points. Each leg with ground contact is +10 points. Firing the main engine is -0.3 points each frame. Firing the side engine is -0.03 points each frame. Solved is 200 points.


Credits
Created by Oleg Klimov.