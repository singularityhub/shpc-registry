---
layout: container
name:  "quay.io/biocontainers/phispy"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/phispy/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/phispy/container.yaml"
updated_at: "2022-11-23 00:21:49.861516"
latest: "4.2.21--py39hc16433a_1"
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
description: "shpc-registry automated BioContainers addition for phispy"
config: {"url": "https://biocontainers.pro/tools/phispy", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for phispy", "latest": {"4.2.21--py39hc16433a_1": "sha256:74e4f0c952d216c32b96d85575b1bc254d106d3e1e5ff36d65a401a991b5fef7"}, "tags": {"4.2.6--py36hae55d0a_1": "sha256:998468b17ab66ce4a3d725ebe5620b2e813c549376069bd7aa7a6e626f225b7a", "4.2.21--py39hc16433a_1": "sha256:74e4f0c952d216c32b96d85575b1bc254d106d3e1e5ff36d65a401a991b5fef7"}, "docker": "quay.io/biocontainers/phispy", "aliases": {"PhiSpy.py": "/usr/local/bin/PhiSpy.py", "compare_predictions_to_phages.py": "/usr/local/bin/compare_predictions_to_phages.py", "make_training_sets.py": "/usr/local/bin/make_training_sets.py", "mark_prophage_features.py": "/usr/local/bin/mark_prophage_features.py", "plot_stats.py": "/usr/local/bin/plot_stats.py", "f2py3.6": "/usr/local/bin/f2py3.6", "2to3-3.6": "/usr/local/bin/2to3-3.6", "idle3.6": "/usr/local/bin/idle3.6", "pydoc3.6": "/usr/local/bin/pydoc3.6", "python3.6": "/usr/local/bin/python3.6", "python3.6-config": "/usr/local/bin/python3.6-config", "python3.6m": "/usr/local/bin/python3.6m", "python3.6m-config": "/usr/local/bin/python3.6m-config", "pyvenv-3.6": "/usr/local/bin/pyvenv-3.6", "pyvenv": "/usr/local/bin/pyvenv"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/phispy.
shpc-registry automated BioContainers addition for phispy
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/phispy
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/phispy:4.2.21--py39hc16433a_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/phispy/4.2.21--py39hc16433a_1
$ module help quay.io/biocontainers/phispy/4.2.21--py39hc16433a_1
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