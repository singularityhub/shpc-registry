---
layout: container
name:  "quay.io/biocontainers/bioconductor-scrnaseqapp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-scrnaseqapp/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-scrnaseqapp/container.yaml"
updated_at: "2025-01-16 03:21:43.724358"
latest: "1.6.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-scrnaseqapp"
aliases:
 - "h5delete"
 - "geosop"
 - "aec"
 - "geos-config"
 - "hb-info"
 - "tjbench"
 - "glpsol"
 - "2to3-3.11"
 - "idle3.11"
 - "pydoc3.11"
 - "python3.11"
 - "python3.11-config"
 - "installBiocDataPackage.sh"
 - "tomlq"
 - "xq"
 - "yq"
 - "jq"
 - "onig-config"
 - "activate-global-python-argcomplete"
 - "python-argcomplete-check-easy-install-script"
 - "register-python-argcomplete"
 - "pandoc"
 - "h5clear"
 - "h5format_convert"
 - "h5watch"
versions:
 - "1.0.1--r43hdfd78af_0"
 - "1.2.2--r43hdfd78af_0"
 - "1.6.0--r44hdfd78af_0"
description: "singularity registry hpc automated addition for bioconductor-scrnaseqapp"
config: {"url": "https://biocontainers.pro/tools/bioconductor-scrnaseqapp", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for bioconductor-scrnaseqapp", "latest": {"1.6.0--r44hdfd78af_0": "sha256:641beec963f45f668a93ac6479febb133d8077c301b53ff4d25fb7be9de34a91"}, "tags": {"1.0.1--r43hdfd78af_0": "sha256:2a454057c9a681e20c1c4ddc57a113f156cb1708fc28a364197f4ddbeeab3674", "1.2.2--r43hdfd78af_0": "sha256:8e941ba759a233b8c5b537b72197ae1fdf1f8995df0726ba18a532a0c69b8cab", "1.6.0--r44hdfd78af_0": "sha256:641beec963f45f668a93ac6479febb133d8077c301b53ff4d25fb7be9de34a91"}, "docker": "quay.io/biocontainers/bioconductor-scrnaseqapp", "aliases": {"h5delete": "/usr/local/bin/h5delete", "geosop": "/usr/local/bin/geosop", "aec": "/usr/local/bin/aec", "geos-config": "/usr/local/bin/geos-config", "hb-info": "/usr/local/bin/hb-info", "tjbench": "/usr/local/bin/tjbench", "glpsol": "/usr/local/bin/glpsol", "2to3-3.11": "/usr/local/bin/2to3-3.11", "idle3.11": "/usr/local/bin/idle3.11", "pydoc3.11": "/usr/local/bin/pydoc3.11", "python3.11": "/usr/local/bin/python3.11", "python3.11-config": "/usr/local/bin/python3.11-config", "installBiocDataPackage.sh": "/usr/local/bin/installBiocDataPackage.sh", "tomlq": "/usr/local/bin/tomlq", "xq": "/usr/local/bin/xq", "yq": "/usr/local/bin/yq", "jq": "/usr/local/bin/jq", "onig-config": "/usr/local/bin/onig-config", "activate-global-python-argcomplete": "/usr/local/bin/activate-global-python-argcomplete", "python-argcomplete-check-easy-install-script": "/usr/local/bin/python-argcomplete-check-easy-install-script", "register-python-argcomplete": "/usr/local/bin/register-python-argcomplete", "pandoc": "/usr/local/bin/pandoc", "h5clear": "/usr/local/bin/h5clear", "h5format_convert": "/usr/local/bin/h5format_convert", "h5watch": "/usr/local/bin/h5watch"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-scrnaseqapp.
singularity registry hpc automated addition for bioconductor-scrnaseqapp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-scrnaseqapp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-scrnaseqapp:1.6.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-scrnaseqapp/1.6.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-scrnaseqapp/1.6.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-scrnaseqapp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-scrnaseqapp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-scrnaseqapp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-scrnaseqapp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-scrnaseqapp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-scrnaseqapp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### h5delete

```bash
$ singularity exec <container> /usr/local/bin/h5delete
$ podman run --it --rm --entrypoint /usr/local/bin/h5delete   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5delete   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### geosop

```bash
$ singularity exec <container> /usr/local/bin/geosop
$ podman run --it --rm --entrypoint /usr/local/bin/geosop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/geosop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aec

```bash
$ singularity exec <container> /usr/local/bin/aec
$ podman run --it --rm --entrypoint /usr/local/bin/aec   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aec   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### geos-config

```bash
$ singularity exec <container> /usr/local/bin/geos-config
$ podman run --it --rm --entrypoint /usr/local/bin/geos-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/geos-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### glpsol

```bash
$ singularity exec <container> /usr/local/bin/glpsol
$ podman run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.11

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.11
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.11

```bash
$ singularity exec <container> /usr/local/bin/idle3.11
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.11

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.11
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.11

```bash
$ singularity exec <container> /usr/local/bin/python3.11
$ podman run --it --rm --entrypoint /usr/local/bin/python3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.11-config

```bash
$ singularity exec <container> /usr/local/bin/python3.11-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.11-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.11-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### pandoc

```bash
$ singularity exec <container> /usr/local/bin/pandoc
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5clear

```bash
$ singularity exec <container> /usr/local/bin/h5clear
$ podman run --it --rm --entrypoint /usr/local/bin/h5clear   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5clear   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5format_convert

```bash
$ singularity exec <container> /usr/local/bin/h5format_convert
$ podman run --it --rm --entrypoint /usr/local/bin/h5format_convert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5format_convert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5watch

```bash
$ singularity exec <container> /usr/local/bin/h5watch
$ podman run --it --rm --entrypoint /usr/local/bin/h5watch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5watch   -v ${PWD} -w ${PWD} <container> -c " $@"
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