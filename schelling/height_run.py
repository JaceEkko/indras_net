#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 18 16:45:50 2014

@author: Gene Callahan and Brandon Logan
"""
MODEL_NM = "Schelling Height"

import indra.prop_args as props
pa = props.PropArgs.create_props(MODEL_NM)

import indra.utils as utils
import indra.prop_args as props
import schelling.height_model as hm

START_HEIGHT = 100.0


def run(prop_dict=None):
    (prog_file, log_file, prop_file, results_file) = utils.gen_file_names(MODEL_NM)
    global pa

    if prop_dict is not None:
        prop_dict[props.PERIODS] = 1
        pa.add_props(prop_dict)
    else:
        result = utils.read_props(MODEL_NM)
        if result:
            pa.add_props(result.props)
        else:
            utils.ask_for_params(pa)
    env = hm.HeightEnv(model_nm=MODEL_NM, props=pa)
    for i in range(pa["num_agents"]):
            env.add_agent(
                hm.HeightAgentEng('Eng agent' + str(i),
                                  START_HEIGHT, START_HEIGHT))
            env.add_agent(
                hm.HeightAgent('agent' + str(i), START_HEIGHT, START_HEIGHT))
    
    return utils.run_model(env, prog_file, results_file)

if __name__ == "__main__":
    run()
