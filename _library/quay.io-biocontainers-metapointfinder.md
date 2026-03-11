---
layout: container
name:  "quay.io/biocontainers/metapointfinder"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/metapointfinder/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/metapointfinder/container.yaml"
updated_at: "2026-03-11 04:36:42.851063"
latest: "1.01--py314r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/metapointfinder"
aliases:
 - "metapointfinder.py"
 - "kma"
 - "kma_index"
 - "kma_shm"
 - "kma_update"
 - "idle3.14"
 - "pydoc3.14"
 - "python3.14"
 - "python3.14-config"
 - "diamond"
 - "x86_64-conda-linux-gnu.cfg"
 - "installBiocDataPackage.sh"
 - "tomlq"
 - "xq"
 - "yq"
 - "idn2"
 - "jq"
 - "onig-config"
 - "activate-global-python-argcomplete"
 - "python-argcomplete-check-easy-install-script"
 - "register-python-argcomplete"
 - "wget"
 - "hb-info"
 - "tjbench"
versions:
 - "1.01--py314r44hdfd78af_0"
description: "singularity registry hpc automated addition for metapointfinder"
config: {"url": "https://biocontainers.pro/tools/metapointfinder", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for metapointfinder", "latest": {"1.01--py314r44hdfd78af_0": "sha256:817a6f3c24793af406a686590212bb5b137bb1e881498edf178c4ef9757095ca"}, "tags": {"1.01--py314r44hdfd78af_0": "sha256:817a6f3c24793af406a686590212bb5b137bb1e881498edf178c4ef9757095ca"}, "docker": "quay.io/biocontainers/metapointfinder", "aliases": {"metapointfinder.py": "/usr/local/bin/metapointfinder.py", "kma": "/usr/local/bin/kma", "kma_index": "/usr/local/bin/kma_index", "kma_shm": "/usr/local/bin/kma_shm", "kma_update": "/usr/local/bin/kma_update", "idle3.14": "/usr/local/bin/idle3.14", "pydoc3.14": "/usr/local/bin/pydoc3.14", "python3.14": "/usr/local/bin/python3.14", "python3.14-config": "/usr/local/bin/python3.14-config", "diamond": "/usr/local/bin/diamond", "x86_64-conda-linux-gnu.cfg": "/usr/local/bin/x86_64-conda-linux-gnu.cfg", "installBiocDataPackage.sh": "/usr/local/bin/installBiocDataPackage.sh", "tomlq": "/usr/local/bin/tomlq", "xq": "/usr/local/bin/xq", "yq": "/usr/local/bin/yq", "idn2": "/usr/local/bin/idn2", "jq": "/usr/local/bin/jq", "onig-config": "/usr/local/bin/onig-config", "activate-global-python-argcomplete": "/usr/local/bin/activate-global-python-argcomplete", "python-argcomplete-check-easy-install-script": "/usr/local/bin/python-argcomplete-check-easy-install-script", "register-python-argcomplete": "/usr/local/bin/register-python-argcomplete", "wget": "/usr/local/bin/wget", "hb-info": "/usr/local/bin/hb-info", "tjbench": "/usr/local/bin/tjbench"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/metapointfinder.
singularity registry hpc automated addition for metapointfinder
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/metapointfinder
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/metapointfinder:1.01--py314r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/metapointfinder/1.01--py314r44hdfd78af_0
$ module help quay.io/biocontainers/metapointfinder/1.01--py314r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### metapointfinder-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### metapointfinder-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### metapointfinder-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### metapointfinder-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### metapointfinder-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### metapointfinder-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### metapointfinder.py

```bash
$ singularity exec <container> /usr/local/bin/metapointfinder.py
$ podman run --it --rm --entrypoint /usr/local/bin/metapointfinder.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metapointfinder.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kma

```bash
$ singularity exec <container> /usr/local/bin/kma
$ podman run --it --rm --entrypoint /usr/local/bin/kma   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kma   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kma_index

```bash
$ singularity exec <container> /usr/local/bin/kma_index
$ podman run --it --rm --entrypoint /usr/local/bin/kma_index   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kma_index   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kma_shm

```bash
$ singularity exec <container> /usr/local/bin/kma_shm
$ podman run --it --rm --entrypoint /usr/local/bin/kma_shm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kma_shm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kma_update

```bash
$ singularity exec <container> /usr/local/bin/kma_update
$ podman run --it --rm --entrypoint /usr/local/bin/kma_update   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kma_update   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.14

```bash
$ singularity exec <container> /usr/local/bin/idle3.14
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.14

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.14
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.14

```bash
$ singularity exec <container> /usr/local/bin/python3.14
$ podman run --it --rm --entrypoint /usr/local/bin/python3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.14-config

```bash
$ singularity exec <container> /usr/local/bin/python3.14-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.14-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.14-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### diamond

```bash
$ singularity exec <container> /usr/local/bin/diamond
$ podman run --it --rm --entrypoint /usr/local/bin/diamond   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/diamond   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### x86_64-conda-linux-gnu.cfg

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda-linux-gnu.cfg
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu.cfg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu.cfg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### installBiocDataPackage.sh

```bash
$ singularity exec <container> /usr/local/bin/installBiocDataPackage.sh
$ podman run --it --rm --entrypoint /usr/local/bin/installBiocDataPackage.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/installBiocDataPackage.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tomlq

```bash
$ singularity exec <container> /usr/local/bin/tomlq
$ podman run --it --rm --entrypoint /usr/local/bin/tomlq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tomlq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xq

```bash
$ singularity exec <container> /usr/local/bin/xq
$ podman run --it --rm --entrypoint /usr/local/bin/xq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### yq

```bash
$ singularity exec <container> /usr/local/bin/yq
$ podman run --it --rm --entrypoint /usr/local/bin/yq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/yq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idn2

```bash
$ singularity exec <container> /usr/local/bin/idn2
$ podman run --it --rm --entrypoint /usr/local/bin/idn2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idn2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jq

```bash
$ singularity exec <container> /usr/local/bin/jq
$ podman run --it --rm --entrypoint /usr/local/bin/jq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### onig-config

```bash
$ singularity exec <container> /usr/local/bin/onig-config
$ podman run --it --rm --entrypoint /usr/local/bin/onig-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/onig-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### activate-global-python-argcomplete

```bash
$ singularity exec <container> /usr/local/bin/activate-global-python-argcomplete
$ podman run --it --rm --entrypoint /usr/local/bin/activate-global-python-argcomplete   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/activate-global-python-argcomplete   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python-argcomplete-check-easy-install-script

```bash
$ singularity exec <container> /usr/local/bin/python-argcomplete-check-easy-install-script
$ podman run --it --rm --entrypoint /usr/local/bin/python-argcomplete-check-easy-install-script   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python-argcomplete-check-easy-install-script   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### register-python-argcomplete

```bash
$ singularity exec <container> /usr/local/bin/register-python-argcomplete
$ podman run --it --rm --entrypoint /usr/local/bin/register-python-argcomplete   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/register-python-argcomplete   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hb-info

```bash
$ singularity exec <container> /usr/local/bin/hb-info
$ podman run --it --rm --entrypoint /usr/local/bin/hb-info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hb-info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tjbench

```bash
$ singularity exec <container> /usr/local/bin/tjbench
$ podman run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
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