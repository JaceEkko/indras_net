#!/usr/bin/env python3
"""
A script to test our grid capabilities.
"""
MODEL_NM = "zombie"

import indra.prop_args2 as props
pa = props.PropArgs.create_props(MODEL_NM)

import indra.utils as utils
import indra.prop_args as props
import models.zombie as zm



def run(prop_dict=None):
    (prog_file, log_file, prop_file, results_file) = utils.gen_file_names(MODEL_NM)
    
    global pa
    
    

if __name__ == "__main__": #python way of establishing main
    run()
