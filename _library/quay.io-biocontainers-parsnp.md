---
layout: container
name:  "quay.io/biocontainers/parsnp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/parsnp/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/parsnp/container.yaml"
updated_at: "2022-10-29 05:33:29.261863"
latest: "1.7.4--hd03093a_1"
container_url: "https://biocontainers.pro/tools/parsnp"
aliases:
 - "Phi"
 - "Profile"
 - "extend.py"
 - "harvesttools"
 - "logger.py"
 - "parsnp"
 - "template.ini"
 - "2to3-3.10"
 - "FastTree"
 - "FastTreeMP"
 - "capnp"
 - "capnpc"
 - "capnpc-c++"
 - "capnpc-capnp"
 - "einsi"
 - "f2py3.10"
 - "fastANI"
versions:
 - "1.7.4--hd03093a_1"
description: "shpc-registry automated BioContainers addition for parsnp"
config: {"url": "https://biocontainers.pro/tools/parsnp", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for parsnp", "latest": {"1.7.4--hd03093a_1": "sha256:92ec26ccc5ad8c73fc010f9deb5594ce9e63874516ca12aad069988256fb5158"}, "tags": {"1.7.4--hd03093a_1": "sha256:92ec26ccc5ad8c73fc010f9deb5594ce9e63874516ca12aad069988256fb5158"}, "docker": "quay.io/biocontainers/parsnp", "aliases": {"Phi": "/usr/local/bin/Phi", "Profile": "/usr/local/bin/Profile", "extend.py": "/usr/local/bin/extend.py", "harvesttools": "/usr/local/bin/harvesttools", "logger.py": "/usr/local/bin/logger.py", "parsnp": "/usr/local/bin/parsnp", "template.ini": "/usr/local/bin/template.ini", "2to3-3.10": "/usr/local/bin/2to3-3.10", "FastTree": "/usr/local/bin/FastTree", "FastTreeMP": "/usr/local/bin/FastTreeMP", "capnp": "/usr/local/bin/capnp", "capnpc": "/usr/local/bin/capnpc", "capnpc-c++": "/usr/local/bin/capnpc-c++", "capnpc-capnp": "/usr/local/bin/capnpc-capnp", "einsi": "/usr/local/bin/einsi", "f2py3.10": "/usr/local/bin/f2py3.10", "fastANI": "/usr/local/bin/fastANI"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/parsnp.
shpc-registry automated BioContainers addition for parsnp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/parsnp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/parsnp:1.7.4--hd03093a_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/parsnp/1.7.4--hd03093a_1
$ module help quay.io/biocontainers/parsnp/1.7.4--hd03093a_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### parsnp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### parsnp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### parsnp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### parsnp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### parsnp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### parsnp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Phi

```bash
$ singularity exec <container> /usr/local/bin/Phi
$ podman run --it --rm --entrypoint /usr/local/bin/Phi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Phi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Profile

```bash
$ singularity exec <container> /usr/local/bin/Profile
$ podman run --it --rm --entrypoint /usr/local/bin/Profile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Profile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extend.py

```bash
$ singularity exec <container> /usr/local/bin/extend.py
$ podman run --it --rm --entrypoint /usr/local/bin/extend.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extend.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### harvesttools

```bash
$ singularity exec <container> /usr/local/bin/harvesttools
$ podman run --it --rm --entrypoint /usr/local/bin/harvesttools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/harvesttools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### logger.py

```bash
$ singularity exec <container> /usr/local/bin/logger.py
$ podman run --it --rm --entrypoint /usr/local/bin/logger.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/logger.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### parsnp

```bash
$ singularity exec <container> /usr/local/bin/parsnp
$ podman run --it --rm --entrypoint /usr/local/bin/parsnp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/parsnp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### template.ini

```bash
$ singularity exec <container> /usr/local/bin/template.ini
$ podman run --it --rm --entrypoint /usr/local/bin/template.ini   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/template.ini   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.10

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.10
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### FastTree

```bash
$ singularity exec <container> /usr/local/bin/FastTree
$ podman run --it --rm --entrypoint /usr/local/bin/FastTree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FastTree   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### FastTreeMP

```bash
$ singularity exec <container> /usr/local/bin/FastTreeMP
$ podman run --it --rm --entrypoint /usr/local/bin/FastTreeMP   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FastTreeMP   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### capnp

```bash
$ singularity exec <container> /usr/local/bin/capnp
$ podman run --it --rm --entrypoint /usr/local/bin/capnp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/capnp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### capnpc

```bash
$ singularity exec <container> /usr/local/bin/capnpc
$ podman run --it --rm --entrypoint /usr/local/bin/capnpc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/capnpc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### capnpc-c++

```bash
$ singularity exec <container> /usr/local/bin/capnpc-c++
$ podman run --it --rm --entrypoint /usr/local/bin/capnpc-c++   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/capnpc-c++   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### capnpc-capnp

```bash
$ singularity exec <container> /usr/local/bin/capnpc-capnp
$ podman run --it --rm --entrypoint /usr/local/bin/capnpc-capnp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/capnpc-capnp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### einsi

```bash
$ singularity exec <container> /usr/local/bin/einsi
$ podman run --it --rm --entrypoint /usr/local/bin/einsi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/einsi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.10

```bash
$ singularity exec <container> /usr/local/bin/f2py3.10
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastANI

```bash
$ singularity exec <container> /usr/local/bin/fastANI
$ podman run --it --rm --entrypoint /usr/local/bin/fastANI   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastANI   -v ${PWD} -w ${PWD} <container> -c " $@"
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