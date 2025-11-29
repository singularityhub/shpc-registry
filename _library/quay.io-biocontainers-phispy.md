---
layout: container
name:  "quay.io/biocontainers/phispy"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/phispy/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/phispy/container.yaml"
updated_at: "2025-11-29 04:05:45.829630"
latest: "4.2.21--py39h2de1943_8"
container_url: "https://biocontainers.pro/tools/phispy"
aliases:
 - "PhiSpy.py"
 - "compare_predictions_to_phages.py"
 - "make_training_sets.py"
 - "mark_prophage_features.py"
 - "plot_stats.py"
 - "f2py3.6"
 - "2to3-3.6"
 - "idle3.6"
 - "pydoc3.6"
 - "python3.6"
 - "python3.6-config"
 - "python3.6m"
 - "python3.6m-config"
 - "pyvenv-3.6"
 - "pyvenv"
versions:
 - "4.2.6--py36hae55d0a_1"
 - "4.2.21--py39hc16433a_1"
 - "4.2.21--py38h2494328_2"
 - "4.2.21--py310h0dbaff4_2"
 - "4.2.21--py38h2494328_3"
 - "4.2.21--py311h2a4ad6c_6"
 - "4.2.21--py39h2de1943_7"
 - "4.2.21--py39h2de1943_8"
description: "shpc-registry automated BioContainers addition for phispy"
config: {"url": "https://biocontainers.pro/tools/phispy", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for phispy", "latest": {"4.2.21--py39h2de1943_8": "sha256:1fff862a40fec2b97049fb05dd5f00af596fdfc84d457f46f386af81f9bc1480"}, "tags": {"4.2.6--py36hae55d0a_1": "sha256:998468b17ab66ce4a3d725ebe5620b2e813c549376069bd7aa7a6e626f225b7a", "4.2.21--py39hc16433a_1": "sha256:74e4f0c952d216c32b96d85575b1bc254d106d3e1e5ff36d65a401a991b5fef7", "4.2.21--py38h2494328_2": "sha256:0a40777ca6bc601d4592a98b87c40d1fa5c776a82417fd0f63b8ed7dccfe8427", "4.2.21--py310h0dbaff4_2": "sha256:303315a5444cba6108f7b65ef1cbc216340bac1034707a3edad0901959ccd6e0", "4.2.21--py38h2494328_3": "sha256:954c1669286f24c0c73c698dffc8b4d59082d47805871505ee3350d1703d41d8", "4.2.21--py311h2a4ad6c_6": "sha256:832fe8f0cc22e0f5622f34b9bca00c6bc1e51420b9b7a0cf8e5dc251dfd42620", "4.2.21--py39h2de1943_7": "sha256:4f5dc9cb539a5bc75d5a6e846786b766e38e99408749c36f247a2da3dc6dbc6c", "4.2.21--py39h2de1943_8": "sha256:1fff862a40fec2b97049fb05dd5f00af596fdfc84d457f46f386af81f9bc1480"}, "docker": "quay.io/biocontainers/phispy", "aliases": {"PhiSpy.py": "/usr/local/bin/PhiSpy.py", "compare_predictions_to_phages.py": "/usr/local/bin/compare_predictions_to_phages.py", "make_training_sets.py": "/usr/local/bin/make_training_sets.py", "mark_prophage_features.py": "/usr/local/bin/mark_prophage_features.py", "plot_stats.py": "/usr/local/bin/plot_stats.py", "f2py3.6": "/usr/local/bin/f2py3.6", "2to3-3.6": "/usr/local/bin/2to3-3.6", "idle3.6": "/usr/local/bin/idle3.6", "pydoc3.6": "/usr/local/bin/pydoc3.6", "python3.6": "/usr/local/bin/python3.6", "python3.6-config": "/usr/local/bin/python3.6-config", "python3.6m": "/usr/local/bin/python3.6m", "python3.6m-config": "/usr/local/bin/python3.6m-config", "pyvenv-3.6": "/usr/local/bin/pyvenv-3.6", "pyvenv": "/usr/local/bin/pyvenv"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/phispy.
shpc-registry automated BioContainers addition for phispy
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/phispy
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/phispy:4.2.21--py39h2de1943_8
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/phispy/4.2.21--py39h2de1943_8
$ module help quay.io/biocontainers/phispy/4.2.21--py39h2de1943_8
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### phispy-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### phispy-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### phispy-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### phispy-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### phispy-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### phispy-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### PhiSpy.py

```bash
$ singularity exec <container> /usr/local/bin/PhiSpy.py
$ podman run --it --rm --entrypoint /usr/local/bin/PhiSpy.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PhiSpy.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### compare_predictions_to_phages.py

```bash
$ singularity exec <container> /usr/local/bin/compare_predictions_to_phages.py
$ podman run --it --rm --entrypoint /usr/local/bin/compare_predictions_to_phages.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compare_predictions_to_phages.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### make_training_sets.py

```bash
$ singularity exec <container> /usr/local/bin/make_training_sets.py
$ podman run --it --rm --entrypoint /usr/local/bin/make_training_sets.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/make_training_sets.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mark_prophage_features.py

```bash
$ singularity exec <container> /usr/local/bin/mark_prophage_features.py
$ podman run --it --rm --entrypoint /usr/local/bin/mark_prophage_features.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mark_prophage_features.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plot_stats.py

```bash
$ singularity exec <container> /usr/local/bin/plot_stats.py
$ podman run --it --rm --entrypoint /usr/local/bin/plot_stats.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot_stats.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.6

```bash
$ singularity exec <container> /usr/local/bin/f2py3.6
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.6

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.6
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.6

```bash
$ singularity exec <container> /usr/local/bin/idle3.6
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.6

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.6
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.6

```bash
$ singularity exec <container> /usr/local/bin/python3.6
$ podman run --it --rm --entrypoint /usr/local/bin/python3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.6-config

```bash
$ singularity exec <container> /usr/local/bin/python3.6-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.6-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.6-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.6m

```bash
$ singularity exec <container> /usr/local/bin/python3.6m
$ podman run --it --rm --entrypoint /usr/local/bin/python3.6m   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.6m   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.6m-config

```bash
$ singularity exec <container> /usr/local/bin/python3.6m-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.6m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.6m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyvenv-3.6

```bash
$ singularity exec <container> /usr/local/bin/pyvenv-3.6
$ podman run --it --rm --entrypoint /usr/local/bin/pyvenv-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyvenv-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyvenv

```bash
$ singularity exec <container> /usr/local/bin/pyvenv
$ podman run --it --rm --entrypoint /usr/local/bin/pyvenv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyvenv   -v ${PWD} -w ${PWD} <container> -c " $@"
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