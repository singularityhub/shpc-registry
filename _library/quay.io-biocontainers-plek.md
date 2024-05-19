---
layout: container
name:  "quay.io/biocontainers/plek"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/plek/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/plek/container.yaml"
updated_at: "2024-05-19 02:34:08.408486"
latest: "1.2--py39he10ea66_7"
container_url: "https://biocontainers.pro/tools/plek"
aliases:
 - "PLEK"
 - "PLEK.model"
 - "PLEK.py"
 - "PLEK.range"
 - "PLEKModelling.py"
 - "PLEK_generate_scripts.R"
 - "PLEK_setup.py"
 - "PLEK_spsn"
 - "svm-easy.py"
 - "svm-subset.py"
 - "svm_grid_modelling.py"
 - "svm_grid_modelling_singlet.py"
 - "svm-predict"
 - "svm-scale"
 - "svm-train"
 - "2to3-3.8"
 - "idle3.8"
 - "pydoc3.8"
 - "python3.8"
 - "python3.8-config"
versions:
 - "1.2--py38h8ded8fe_5"
 - "1.2--py39he10ea66_7"
 - "1.2--py38hcbe9525_7"
description: "shpc-registry automated BioContainers addition for plek"
config: {"url": "https://biocontainers.pro/tools/plek", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for plek", "latest": {"1.2--py39he10ea66_7": "sha256:dcb1a49e121b4627a7ed12bba2ca796265812325391ab6160ddb53ebaf755392"}, "tags": {"1.2--py38h8ded8fe_5": "sha256:ac9e43073c12cd1936311ae7b2dc6dc247c424467aead24ebf6ffd790e8620f9", "1.2--py39he10ea66_7": "sha256:dcb1a49e121b4627a7ed12bba2ca796265812325391ab6160ddb53ebaf755392", "1.2--py38hcbe9525_7": "sha256:afccd6ad0e4c69bc77636169ead8ee9668888bd5bc4f5bc58881bdda56b238d7"}, "docker": "quay.io/biocontainers/plek", "aliases": {"PLEK": "/usr/local/bin/PLEK", "PLEK.model": "/usr/local/bin/PLEK.model", "PLEK.py": "/usr/local/bin/PLEK.py", "PLEK.range": "/usr/local/bin/PLEK.range", "PLEKModelling.py": "/usr/local/bin/PLEKModelling.py", "PLEK_generate_scripts.R": "/usr/local/bin/PLEK_generate_scripts.R", "PLEK_setup.py": "/usr/local/bin/PLEK_setup.py", "PLEK_spsn": "/usr/local/bin/PLEK_spsn", "svm-easy.py": "/usr/local/bin/svm-easy.py", "svm-subset.py": "/usr/local/bin/svm-subset.py", "svm_grid_modelling.py": "/usr/local/bin/svm_grid_modelling.py", "svm_grid_modelling_singlet.py": "/usr/local/bin/svm_grid_modelling_singlet.py", "svm-predict": "/usr/local/bin/svm-predict", "svm-scale": "/usr/local/bin/svm-scale", "svm-train": "/usr/local/bin/svm-train", "2to3-3.8": "/usr/local/bin/2to3-3.8", "idle3.8": "/usr/local/bin/idle3.8", "pydoc3.8": "/usr/local/bin/pydoc3.8", "python3.8": "/usr/local/bin/python3.8", "python3.8-config": "/usr/local/bin/python3.8-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/plek.
shpc-registry automated BioContainers addition for plek
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/plek
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/plek:1.2--py39he10ea66_7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/plek/1.2--py39he10ea66_7
$ module help quay.io/biocontainers/plek/1.2--py39he10ea66_7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### plek-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### plek-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### plek-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### plek-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### plek-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### plek-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### PLEK

```bash
$ singularity exec <container> /usr/local/bin/PLEK
$ podman run --it --rm --entrypoint /usr/local/bin/PLEK   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PLEK   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PLEK.model

```bash
$ singularity exec <container> /usr/local/bin/PLEK.model
$ podman run --it --rm --entrypoint /usr/local/bin/PLEK.model   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PLEK.model   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PLEK.py

```bash
$ singularity exec <container> /usr/local/bin/PLEK.py
$ podman run --it --rm --entrypoint /usr/local/bin/PLEK.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PLEK.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PLEK.range

```bash
$ singularity exec <container> /usr/local/bin/PLEK.range
$ podman run --it --rm --entrypoint /usr/local/bin/PLEK.range   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PLEK.range   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PLEKModelling.py

```bash
$ singularity exec <container> /usr/local/bin/PLEKModelling.py
$ podman run --it --rm --entrypoint /usr/local/bin/PLEKModelling.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PLEKModelling.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PLEK_generate_scripts.R

```bash
$ singularity exec <container> /usr/local/bin/PLEK_generate_scripts.R
$ podman run --it --rm --entrypoint /usr/local/bin/PLEK_generate_scripts.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PLEK_generate_scripts.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PLEK_setup.py

```bash
$ singularity exec <container> /usr/local/bin/PLEK_setup.py
$ podman run --it --rm --entrypoint /usr/local/bin/PLEK_setup.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PLEK_setup.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PLEK_spsn

```bash
$ singularity exec <container> /usr/local/bin/PLEK_spsn
$ podman run --it --rm --entrypoint /usr/local/bin/PLEK_spsn   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PLEK_spsn   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### svm-easy.py

```bash
$ singularity exec <container> /usr/local/bin/svm-easy.py
$ podman run --it --rm --entrypoint /usr/local/bin/svm-easy.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/svm-easy.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### svm-subset.py

```bash
$ singularity exec <container> /usr/local/bin/svm-subset.py
$ podman run --it --rm --entrypoint /usr/local/bin/svm-subset.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/svm-subset.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### svm_grid_modelling.py

```bash
$ singularity exec <container> /usr/local/bin/svm_grid_modelling.py
$ podman run --it --rm --entrypoint /usr/local/bin/svm_grid_modelling.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/svm_grid_modelling.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### svm_grid_modelling_singlet.py

```bash
$ singularity exec <container> /usr/local/bin/svm_grid_modelling_singlet.py
$ podman run --it --rm --entrypoint /usr/local/bin/svm_grid_modelling_singlet.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/svm_grid_modelling_singlet.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### svm-predict

```bash
$ singularity exec <container> /usr/local/bin/svm-predict
$ podman run --it --rm --entrypoint /usr/local/bin/svm-predict   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/svm-predict   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### svm-scale

```bash
$ singularity exec <container> /usr/local/bin/svm-scale
$ podman run --it --rm --entrypoint /usr/local/bin/svm-scale   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/svm-scale   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### svm-train

```bash
$ singularity exec <container> /usr/local/bin/svm-train
$ podman run --it --rm --entrypoint /usr/local/bin/svm-train   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/svm-train   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.8

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.8
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.8

```bash
$ singularity exec <container> /usr/local/bin/idle3.8
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.8

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.8
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.8

```bash
$ singularity exec <container> /usr/local/bin/python3.8
$ podman run --it --rm --entrypoint /usr/local/bin/python3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.8-config

```bash
$ singularity exec <container> /usr/local/bin/python3.8-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.8-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.8-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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