"""Examples demonstrating the usage of RE3 exploration strategy.

To use RE3 user will need to patch the callbacks with RE3 specific callbacks
and set the `exploration_config` with RE3 configs.

```Python

config["exploration_config"] = {"type": "RE3"}
"""
from functools import partial
import ray
from ray.rllib.algorithms import sac
from ray.rllib.algorithms.callbacks import MultiCallbacks, RE3UpdateCallbacks

if __name__ == "__main__":
    ray.init()

    config = (
        sac.SACConfig()
        .environment("LunarLanderContinuous-v2")
        # Add type as RE3 in the exploration_config parameter
        .exploration(
            exploration_config={
                "type": "RE3",
                "sub_exploration": {
                    "type": "StochasticSampling",
                },
            }
        )
        .debugging(seed=12345)
    )

    # Add a new RE3UpdateCallbacks
    config.callbacks(
        MultiCallbacks(
            [
                config.callbacks_class,
                partial(
                    RE3UpdateCallbacks,
                    embeds_dim=128,
                    beta_schedule="linear_decay",
                    k_nn=50,
                ),
            ]
        )
    )

    num_iterations = 2000
    algo = config.build()
    for i in range(num_iterations):
        result = algo.train()
        print(result)
    algo.stop()
    ray.shutdown()
