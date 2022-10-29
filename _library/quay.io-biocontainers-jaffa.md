---
layout: container
name:  "quay.io/biocontainers/jaffa"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/jaffa/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/jaffa/container.yaml"
updated_at: "2022-10-29 05:55:55.883047"
latest: "2.3--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/jaffa"
aliases:
 - "bg-bpipe"
 - "bpipe"
 - "bpipe-groovy"
 - "bpipe-pbspro.sh"
 - "bpipe-slurm.sh"
 - "bpipe-torque.sh"
 - "bpipe-utils.sh"
 - "faToNib"
 - "gfClient"
 - "groovy_script"
 - "jaffa-assembly"
 - "jaffa-direct"
 - "jaffa-hybrid"
 - "nibFrag"
 - "oases"
 - "oases_pipeline.py"
 - "pslPretty"
 - "pslReps"
 - "a_sample_mt.sh"
 - "addadapters.sh"
 - "addssu.sh"
 - "adjusthomopolymers.sh"
 - "alltoall.sh"
 - "analyzeaccession.sh"
 - "analyzegenes.sh"
 - "analyzesketchresults.sh"
 - "applyvariants.sh"
 - "aserver"
versions:
 - "2.3--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for jaffa"
config: {"url": "https://biocontainers.pro/tools/jaffa", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for jaffa", "latest": {"2.3--hdfd78af_0": "sha256:cc18a8fbacf34b8bc0439bd2d92fb5a48facc36a2c88e7abfc7c7382cfe2335d"}, "tags": {"2.3--hdfd78af_0": "sha256:cc18a8fbacf34b8bc0439bd2d92fb5a48facc36a2c88e7abfc7c7382cfe2335d"}, "docker": "quay.io/biocontainers/jaffa", "aliases": {"bg-bpipe": "/usr/local/bin/bg-bpipe", "bpipe": "/usr/local/bin/bpipe", "bpipe-groovy": "/usr/local/bin/bpipe-groovy", "bpipe-pbspro.sh": "/usr/local/bin/bpipe-pbspro.sh", "bpipe-slurm.sh": "/usr/local/bin/bpipe-slurm.sh", "bpipe-torque.sh": "/usr/local/bin/bpipe-torque.sh", "bpipe-utils.sh": "/usr/local/bin/bpipe-utils.sh", "faToNib": "/usr/local/bin/faToNib", "gfClient": "/usr/local/bin/gfClient", "groovy_script": "/usr/local/bin/groovy_script", "jaffa-assembly": "/usr/local/bin/jaffa-assembly", "jaffa-direct": "/usr/local/bin/jaffa-direct", "jaffa-hybrid": "/usr/local/bin/jaffa-hybrid", "nibFrag": "/usr/local/bin/nibFrag", "oases": "/usr/local/bin/oases", "oases_pipeline.py": "/usr/local/bin/oases_pipeline.py", "pslPretty": "/usr/local/bin/pslPretty", "pslReps": "/usr/local/bin/pslReps", "a_sample_mt.sh": "/usr/local/bin/a_sample_mt.sh", "addadapters.sh": "/usr/local/bin/addadapters.sh", "addssu.sh": "/usr/local/bin/addssu.sh", "adjusthomopolymers.sh": "/usr/local/bin/adjusthomopolymers.sh", "alltoall.sh": "/usr/local/bin/alltoall.sh", "analyzeaccession.sh": "/usr/local/bin/analyzeaccession.sh", "analyzegenes.sh": "/usr/local/bin/analyzegenes.sh", "analyzesketchresults.sh": "/usr/local/bin/analyzesketchresults.sh", "applyvariants.sh": "/usr/local/bin/applyvariants.sh", "aserver": "/usr/local/bin/aserver"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/jaffa.
shpc-registry automated BioContainers addition for jaffa
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/jaffa
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/jaffa:2.3--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/jaffa/2.3--hdfd78af_0
$ module help quay.io/biocontainers/jaffa/2.3--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### jaffa-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### jaffa-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### jaffa-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### jaffa-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### jaffa-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### jaffa-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bg-bpipe

```bash
$ singularity exec <container> /usr/local/bin/bg-bpipe
$ podman run --it --rm --entrypoint /usr/local/bin/bg-bpipe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bg-bpipe   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bpipe

```bash
$ singularity exec <container> /usr/local/bin/bpipe
$ podman run --it --rm --entrypoint /usr/local/bin/bpipe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bpipe   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bpipe-groovy

```bash
$ singularity exec <container> /usr/local/bin/bpipe-groovy
$ podman run --it --rm --entrypoint /usr/local/bin/bpipe-groovy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bpipe-groovy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bpipe-pbspro.sh

```bash
$ singularity exec <container> /usr/local/bin/bpipe-pbspro.sh
$ podman run --it --rm --entrypoint /usr/local/bin/bpipe-pbspro.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bpipe-pbspro.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bpipe-slurm.sh

```bash
$ singularity exec <container> /usr/local/bin/bpipe-slurm.sh
$ podman run --it --rm --entrypoint /usr/local/bin/bpipe-slurm.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bpipe-slurm.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bpipe-torque.sh

```bash
$ singularity exec <container> /usr/local/bin/bpipe-torque.sh
$ podman run --it --rm --entrypoint /usr/local/bin/bpipe-torque.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bpipe-torque.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bpipe-utils.sh

```bash
$ singularity exec <container> /usr/local/bin/bpipe-utils.sh
$ podman run --it --rm --entrypoint /usr/local/bin/bpipe-utils.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bpipe-utils.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### faToNib

```bash
$ singularity exec <container> /usr/local/bin/faToNib
$ podman run --it --rm --entrypoint /usr/local/bin/faToNib   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/faToNib   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gfClient

```bash
$ singularity exec <container> /usr/local/bin/gfClient
$ podman run --it --rm --entrypoint /usr/local/bin/gfClient   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gfClient   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### groovy_script

```bash
$ singularity exec <container> /usr/local/bin/groovy_script
$ podman run --it --rm --entrypoint /usr/local/bin/groovy_script   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/groovy_script   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jaffa-assembly

```bash
$ singularity exec <container> /usr/local/bin/jaffa-assembly
$ podman run --it --rm --entrypoint /usr/local/bin/jaffa-assembly   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jaffa-assembly   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jaffa-direct

```bash
$ singularity exec <container> /usr/local/bin/jaffa-direct
$ podman run --it --rm --entrypoint /usr/local/bin/jaffa-direct   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jaffa-direct   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jaffa-hybrid

```bash
$ singularity exec <container> /usr/local/bin/jaffa-hybrid
$ podman run --it --rm --entrypoint /usr/local/bin/jaffa-hybrid   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jaffa-hybrid   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nibFrag

```bash
$ singularity exec <container> /usr/local/bin/nibFrag
$ podman run --it --rm --entrypoint /usr/local/bin/nibFrag   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nibFrag   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### oases

```bash
$ singularity exec <container> /usr/local/bin/oases
$ podman run --it --rm --entrypoint /usr/local/bin/oases   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/oases   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### oases_pipeline.py

```bash
$ singularity exec <container> /usr/local/bin/oases_pipeline.py
$ podman run --it --rm --entrypoint /usr/local/bin/oases_pipeline.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/oases_pipeline.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pslPretty

```bash
$ singularity exec <container> /usr/local/bin/pslPretty
$ podman run --it --rm --entrypoint /usr/local/bin/pslPretty   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pslPretty   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pslReps

```bash
$ singularity exec <container> /usr/local/bin/pslReps
$ podman run --it --rm --entrypoint /usr/local/bin/pslReps   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pslReps   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### a_sample_mt.sh

```bash
$ singularity exec <container> /usr/local/bin/a_sample_mt.sh
$ podman run --it --rm --entrypoint /usr/local/bin/a_sample_mt.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/a_sample_mt.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### addadapters.sh

```bash
$ singularity exec <container> /usr/local/bin/addadapters.sh
$ podman run --it --rm --entrypoint /usr/local/bin/addadapters.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/addadapters.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### addssu.sh

```bash
$ singularity exec <container> /usr/local/bin/addssu.sh
$ podman run --it --rm --entrypoint /usr/local/bin/addssu.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/addssu.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### adjusthomopolymers.sh

```bash
$ singularity exec <container> /usr/local/bin/adjusthomopolymers.sh
$ podman run --it --rm --entrypoint /usr/local/bin/adjusthomopolymers.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/adjusthomopolymers.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### alltoall.sh

```bash
$ singularity exec <container> /usr/local/bin/alltoall.sh
$ podman run --it --rm --entrypoint /usr/local/bin/alltoall.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/alltoall.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### analyzeaccession.sh

```bash
$ singularity exec <container> /usr/local/bin/analyzeaccession.sh
$ podman run --it --rm --entrypoint /usr/local/bin/analyzeaccession.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/analyzeaccession.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### analyzegenes.sh

```bash
$ singularity exec <container> /usr/local/bin/analyzegenes.sh
$ podman run --it --rm --entrypoint /usr/local/bin/analyzegenes.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/analyzegenes.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### analyzesketchresults.sh

```bash
$ singularity exec <container> /usr/local/bin/analyzesketchresults.sh
$ podman run --it --rm --entrypoint /usr/local/bin/analyzesketchresults.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/analyzesketchresults.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### applyvariants.sh

```bash
$ singularity exec <container> /usr/local/bin/applyvariants.sh
$ podman run --it --rm --entrypoint /usr/local/bin/applyvariants.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/applyvariants.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aserver

```bash
$ singularity exec <container> /usr/local/bin/aserver
$ podman run --it --rm --entrypoint /usr/local/bin/aserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aserver   -v ${PWD} -w ${PWD} <container> -c " $@"
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