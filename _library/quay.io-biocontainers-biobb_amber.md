---
layout: container
name:  "quay.io/biocontainers/biobb_amber"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/biobb_amber/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/biobb_amber/container.yaml"
updated_at: "2022-10-27 00:51:02.000928"
latest: "3.8.0--pyhdfd78af_1"
container_url: "https://biocontainers.pro/tools/biobb_amber"
aliases:
 - "MMPBSA.py.MPI"
 - "amber_to_pdb"
 - "bar_pbsa.py"
 - "cestats_run"
 - "cphstats_run"
 - "cpptraj_randomize_ions"
 - "leap_add_ions"
 - "leap_build_linear_structure"
 - "leap_gen_top"
 - "leap_solvate"
 - "makeCHIR_RST"
 - "makeCSA_RST.na"
 - "makeDIP_RST.dna"
 - "makeDIP_RST.protein"
 - "makeRIGID_RST"
 - "nab_build_dna_structure"
 - "parmed_cpinutil"
 - "parmed_hmassrepartition"
 - "pdb4amber_run"
 - "pmemd_mdrun"
 - "process_mdout"
 - "process_minout"
 - "py_resp.py"
 - "sander_mdrun"
 - "tinker_to_amber"
versions:
 - "3.8.0--pyhdfd78af_1"
description: "shpc-registry automated BioContainers addition for biobb_amber"
config: {"url": "https://biocontainers.pro/tools/biobb_amber", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for biobb_amber", "latest": {"3.8.0--pyhdfd78af_1": "sha256:191b3a2664ed3f62929addfc23fc8c300ec8a942d15a6394136a83638584126c"}, "tags": {"3.8.0--pyhdfd78af_1": "sha256:191b3a2664ed3f62929addfc23fc8c300ec8a942d15a6394136a83638584126c"}, "docker": "quay.io/biocontainers/biobb_amber", "aliases": {"MMPBSA.py.MPI": "/usr/local/bin/MMPBSA.py.MPI", "amber_to_pdb": "/usr/local/bin/amber_to_pdb", "bar_pbsa.py": "/usr/local/bin/bar_pbsa.py", "cestats_run": "/usr/local/bin/cestats_run", "cphstats_run": "/usr/local/bin/cphstats_run", "cpptraj_randomize_ions": "/usr/local/bin/cpptraj_randomize_ions", "leap_add_ions": "/usr/local/bin/leap_add_ions", "leap_build_linear_structure": "/usr/local/bin/leap_build_linear_structure", "leap_gen_top": "/usr/local/bin/leap_gen_top", "leap_solvate": "/usr/local/bin/leap_solvate", "makeCHIR_RST": "/usr/local/bin/makeCHIR_RST", "makeCSA_RST.na": "/usr/local/bin/makeCSA_RST.na", "makeDIP_RST.dna": "/usr/local/bin/makeDIP_RST.dna", "makeDIP_RST.protein": "/usr/local/bin/makeDIP_RST.protein", "makeRIGID_RST": "/usr/local/bin/makeRIGID_RST", "nab_build_dna_structure": "/usr/local/bin/nab_build_dna_structure", "parmed_cpinutil": "/usr/local/bin/parmed_cpinutil", "parmed_hmassrepartition": "/usr/local/bin/parmed_hmassrepartition", "pdb4amber_run": "/usr/local/bin/pdb4amber_run", "pmemd_mdrun": "/usr/local/bin/pmemd_mdrun", "process_mdout": "/usr/local/bin/process_mdout", "process_minout": "/usr/local/bin/process_minout", "py_resp.py": "/usr/local/bin/py_resp.py", "sander_mdrun": "/usr/local/bin/sander_mdrun", "tinker_to_amber": "/usr/local/bin/tinker_to_amber"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/biobb_amber.
shpc-registry automated BioContainers addition for biobb_amber
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/biobb_amber
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/biobb_amber:3.8.0--pyhdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/biobb_amber/3.8.0--pyhdfd78af_1
$ module help quay.io/biocontainers/biobb_amber/3.8.0--pyhdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### biobb_amber-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### biobb_amber-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### biobb_amber-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### biobb_amber-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### biobb_amber-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### biobb_amber-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### MMPBSA.py.MPI

```bash
$ singularity exec <container> /usr/local/bin/MMPBSA.py.MPI
$ podman run --it --rm --entrypoint /usr/local/bin/MMPBSA.py.MPI   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MMPBSA.py.MPI   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### amber_to_pdb

```bash
$ singularity exec <container> /usr/local/bin/amber_to_pdb
$ podman run --it --rm --entrypoint /usr/local/bin/amber_to_pdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/amber_to_pdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bar_pbsa.py

```bash
$ singularity exec <container> /usr/local/bin/bar_pbsa.py
$ podman run --it --rm --entrypoint /usr/local/bin/bar_pbsa.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bar_pbsa.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cestats_run

```bash
$ singularity exec <container> /usr/local/bin/cestats_run
$ podman run --it --rm --entrypoint /usr/local/bin/cestats_run   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cestats_run   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cphstats_run

```bash
$ singularity exec <container> /usr/local/bin/cphstats_run
$ podman run --it --rm --entrypoint /usr/local/bin/cphstats_run   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cphstats_run   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cpptraj_randomize_ions

```bash
$ singularity exec <container> /usr/local/bin/cpptraj_randomize_ions
$ podman run --it --rm --entrypoint /usr/local/bin/cpptraj_randomize_ions   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cpptraj_randomize_ions   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### leap_add_ions

```bash
$ singularity exec <container> /usr/local/bin/leap_add_ions
$ podman run --it --rm --entrypoint /usr/local/bin/leap_add_ions   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/leap_add_ions   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### leap_build_linear_structure

```bash
$ singularity exec <container> /usr/local/bin/leap_build_linear_structure
$ podman run --it --rm --entrypoint /usr/local/bin/leap_build_linear_structure   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/leap_build_linear_structure   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### leap_gen_top

```bash
$ singularity exec <container> /usr/local/bin/leap_gen_top
$ podman run --it --rm --entrypoint /usr/local/bin/leap_gen_top   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/leap_gen_top   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### leap_solvate

```bash
$ singularity exec <container> /usr/local/bin/leap_solvate
$ podman run --it --rm --entrypoint /usr/local/bin/leap_solvate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/leap_solvate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### makeCHIR_RST

```bash
$ singularity exec <container> /usr/local/bin/makeCHIR_RST
$ podman run --it --rm --entrypoint /usr/local/bin/makeCHIR_RST   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/makeCHIR_RST   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### makeCSA_RST.na

```bash
$ singularity exec <container> /usr/local/bin/makeCSA_RST.na
$ podman run --it --rm --entrypoint /usr/local/bin/makeCSA_RST.na   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/makeCSA_RST.na   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### makeDIP_RST.dna

```bash
$ singularity exec <container> /usr/local/bin/makeDIP_RST.dna
$ podman run --it --rm --entrypoint /usr/local/bin/makeDIP_RST.dna   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/makeDIP_RST.dna   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### makeDIP_RST.protein

```bash
$ singularity exec <container> /usr/local/bin/makeDIP_RST.protein
$ podman run --it --rm --entrypoint /usr/local/bin/makeDIP_RST.protein   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/makeDIP_RST.protein   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### makeRIGID_RST

```bash
$ singularity exec <container> /usr/local/bin/makeRIGID_RST
$ podman run --it --rm --entrypoint /usr/local/bin/makeRIGID_RST   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/makeRIGID_RST   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nab_build_dna_structure

```bash
$ singularity exec <container> /usr/local/bin/nab_build_dna_structure
$ podman run --it --rm --entrypoint /usr/local/bin/nab_build_dna_structure   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nab_build_dna_structure   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### parmed_cpinutil

```bash
$ singularity exec <container> /usr/local/bin/parmed_cpinutil
$ podman run --it --rm --entrypoint /usr/local/bin/parmed_cpinutil   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/parmed_cpinutil   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### parmed_hmassrepartition

```bash
$ singularity exec <container> /usr/local/bin/parmed_hmassrepartition
$ podman run --it --rm --entrypoint /usr/local/bin/parmed_hmassrepartition   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/parmed_hmassrepartition   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pdb4amber_run

```bash
$ singularity exec <container> /usr/local/bin/pdb4amber_run
$ podman run --it --rm --entrypoint /usr/local/bin/pdb4amber_run   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pdb4amber_run   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pmemd_mdrun

```bash
$ singularity exec <container> /usr/local/bin/pmemd_mdrun
$ podman run --it --rm --entrypoint /usr/local/bin/pmemd_mdrun   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pmemd_mdrun   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### process_mdout

```bash
$ singularity exec <container> /usr/local/bin/process_mdout
$ podman run --it --rm --entrypoint /usr/local/bin/process_mdout   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/process_mdout   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### process_minout

```bash
$ singularity exec <container> /usr/local/bin/process_minout
$ podman run --it --rm --entrypoint /usr/local/bin/process_minout   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/process_minout   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### py_resp.py

```bash
$ singularity exec <container> /usr/local/bin/py_resp.py
$ podman run --it --rm --entrypoint /usr/local/bin/py_resp.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/py_resp.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sander_mdrun

```bash
$ singularity exec <container> /usr/local/bin/sander_mdrun
$ podman run --it --rm --entrypoint /usr/local/bin/sander_mdrun   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sander_mdrun   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tinker_to_amber

```bash
$ singularity exec <container> /usr/local/bin/tinker_to_amber
$ podman run --it --rm --entrypoint /usr/local/bin/tinker_to_amber   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tinker_to_amber   -v ${PWD} -w ${PWD} <container> -c " $@"
```



In the above, the `<container>` directive will reference an actual container provided
by the module, for the version you have chosen to load. An environment file in the
module folder will also be bound. Note that although a container
might provide custom commands, every container exposes unique exec, shell, run, and
inspect aliases. For anycommands above, you can export:

 - SINGULARITY_OPTS: to define custom options for singularity (e.g., --debug)
 - SINGULARITY_COMMAND_OPTS: to define custom options for the command (e.g., -b)
 - PODMAN_OPTS: to define custom options for podman or docker
 - PODMAN_COMMAND_OPTS: to define custom options for the command

<br>

### Install

You can install shpc locally (for yourself or your user base) as follows:

```bash
$ git clone https://github.com/singularityhub/singularity-hpc
$ cd singularity-hpc
$ pip install -e .
```

Have any questions, or want to request a new module or version? [ask for help!](https://github.com/singularityhub/singularity-hpc/issues)