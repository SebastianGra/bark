cc_library(
    name = "base_evaluator",
    hdrs = [
        "base_evaluator.hpp",
    ],
    deps = [
        "//modules/geometry",
        "//modules/commons:commons",
        "@boost//:geometry",
    ],
    visibility = ["//visibility:public"],
)


cc_library(
    name = "evaluator_goal_reached",
    hdrs = [
        "evaluator_goal_reached.hpp",
    ],
    deps = [
        "//modules/world:world",
        ":base_evaluator",
        "@boost//:geometry",

    ],
    visibility = ["//visibility:public"],
)

cc_library(
    name = "evaluator_distance_to_goal",
    hdrs = [
        "evaluator_distance_to_goal.hpp",
    ],
    deps = [
        "//modules/world:world",
        ":base_evaluator",
        "@boost//:geometry",

    ],
    visibility = ["//visibility:public"],
)

cc_library(
    name = "evaluator_behavior_expired",
    hdrs = [
        "evaluator_behavior_expired.hpp",
    ],
    deps = [
        "//modules/world:world",
        "//modules/models/behavior:behavior",
        ":base_evaluator",
        "@boost//:geometry",

    ],
    visibility = ["//visibility:public"],
)

cc_library(
    name = "evaluator_collision_agents",
    hdrs = [
        "evaluator_collision_agents.hpp"
    ],
    srcs = [
        "evaluator_collision_agents.cpp"
    ],
    deps = [
        "//modules/world/evaluation:base_evaluator",
        "//modules/geometry",
        "//modules/commons:commons",
        "@boost//:geometry",
        "//modules/world:world",

    ],
    visibility = ["//visibility:public"],
)

cc_library(
    name = "evaluator_collision_ego_agent",
    hdrs = [
        "evaluator_collision_ego_agent.hpp"
    ],
    srcs = [
        "evaluator_collision_ego_agent.cpp"
    ],
    deps = [
        "//modules/world/evaluation:base_evaluator",
        "//modules/world:world",
        "//modules/geometry",
        "//modules/commons:commons",
        "//modules/models/dynamic:dynamic",
        "@boost//:geometry"
    ],
    visibility = ["//visibility:public"],
)
cc_library(
    name = "evaluator_step_count",
    hdrs = [
        "evaluator_step_count.hpp"
    ],
    deps = [
        "//modules/world/evaluation:base_evaluator",
        "//modules/world:world",
        "//modules/geometry",
        "//modules/commons:commons",
        "//modules/models/dynamic:dynamic",
        "@boost//:geometry"
    ],
    visibility = ["//visibility:public"],
)

cc_library(
    name = "evaluator_drivable_area",
    hdrs = [
        "evaluator_drivable_area.hpp"
    ],
    deps = [
        "//modules/world/evaluation:base_evaluator",
        "//modules/geometry",
        "@boost//:geometry",
        "//modules/world:world",

    ],
    visibility = ["//visibility:public"],
)

cc_library(
    name = "evaluation",
    deps = [
        ":evaluator_goal_reached",
        ":base_evaluator",
        ":evaluator_collision_agents",
        ":evaluator_drivable_area",
        ":evaluator_collision_ego_agent",
        ":evaluator_step_count",
        ":evaluator_behavior_expired",
        ":evaluator_distance_to_goal"
    ],
    visibility = ["//visibility:public"],
)

cc_library(
    name="include",
    hdrs=glob(["*.hpp"]),
    visibility = ["//visibility:public"],
)


