```eval_rst
.. image:: bark_logo.jpg
   :align: center
```

&nbsp;


About BARK
==========================

The core focus of BARK is to develop and benchmark behavior models for autonomous agents -- thus, **B**ehavior Benchm**ARK**.
BARK offers a behavior model-centric simulation framework that enables fast-prototyping and the development of behavior models.
Behavior models can easily be integrated — either using Python or C++.
Various behavior models are available ranging from machine learning to conventional approaches.


## Need

Autonomous agents, such as traffic participants, need to make decisions in uncertain environments having many agents, which might be cooperative or possibly adversarial.
Research in decision making brought up many approaches from the fields of machine learning, game, and control theory.
However, transferring approaches to real-world applications, such as self-driving cars introduces several challenges, that prevent such systems to safely enter the market.
One of the remaining challenges is a quantification of the expected performance of behavior generation approaches under true environmental conditions, e.g. unknown behavior of other participants or uncertainty regarding the observations of the environment.
This challenge is currently approached by driving endless amounts of kilometers in simulation-based and in recorded scenarios.
However, such an approach impedes getting insights into the causes of performance differences of the evaluated approaches.
Implemented improvements of an approach require frequent re-evaluation over the whole set of scenarios.
To make behavior generation approaches ready for the real-world, an analysis framework should be established which can accurately model the divergence between real behavior of other participants and the behaviors generated by models (algorithms).
Such a framework would allow for a more thorough investigation of the expected performance of behavior generation approaches under true environmental conditions.
To make the claims of simulation-based performance results transferable to reality, benchmark scenario specifications must be selected according to certain coverage criteria and agreed on by the whole community of researchers and industry.
BARK tries to tackle and solve the above mentioned challenges and problems.

For more information have a look at our latest paper: [BARK: Open Behavior Benchmarking in Multi-Agent Environments
](https://arxiv.org/abs/2003.02604).


## Approach

BARK is a multi-agent simulation tailored towards the use case of autonomous systems, with a special focus on autonomous driving.
Each agent is controlled by a behavior specification in the form of a behavior model.
Behavioral models can be easily exchanged and used both for simulation of other participants and/or as behavior prediction on the behavior generation side.
For this, BARK defines abstract interfaces for the development of own behavioral models but also delivers several state-of-the-art behavior models based on machine-learning and classical approaches.
By additionally having a set of metrics and functions that evaluate individual components, BARK acts as a comprehensive framework for the development and verification of behavior generation approaches.


## BARK Architecture

BARK has a modular and exchangeable architecture that is composed of modules.
Core modules of BARK:

```eval_rst
.. image:: overview.png
   :width: 100%
   :align: center
```
