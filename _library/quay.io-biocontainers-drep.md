---
layout: container
name:  "quay.io/biocontainers/drep"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/drep/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/drep/container.yaml"
updated_at: "2024-03-20 02:34:06.334687"
latest: "3.5.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/drep"
aliases:
 - "ScaffoldLevel_dRep.py"
 - "dRep"
 - "delta2vcf"
 - "parse_stb.py"
 - "fastANI"
 - "capnp"
 - "capnpc"
 - "capnpc-c++"
 - "capnpc-capnp"
 - "mash"
 - "combineMUMs"
 - "delta-filter"
 - "dnadiff"
 - "exact-tandems"
versions:
 - "3.4.0--pyhdfd78af_0"
 - "3.4.1--pyhdfd78af_0"
 - "3.4.2--pyhdfd78af_0"
 - "3.4.3--pyhdfd78af_0"
 - "3.4.5--pyhdfd78af_0"
 - "3.5.0--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for drep"
config: {"url": "https://biocontainers.pro/tools/drep", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for drep", "latest": {"3.5.0--pyhdfd78af_0": "sha256:3b10a85055a1bc351d4f481c4a93ae04882a3b29e361df7fd0989a30d52ae6dc"}, "tags": {"3.4.0--pyhdfd78af_0": "sha256:29cd012e834f5597788386baf4fec63a2b83dde450d01f1c66648f0acaee4bbc", "3.4.1--pyhdfd78af_0": "sha256:4745a10ed825afb1eda729190aa45a180a20125339cfa6e99698d3afe73cde34", "3.4.2--pyhdfd78af_0": "sha256:d60f32191a9482fd7f008138ae815cb2309aefc900fe4bd54ad82d869909f7f7", "3.4.3--pyhdfd78af_0": "sha256:5cb37e910f309ccdc7119f684b56d433ae9fdabad047d7dbd24ae10de3c3a5ad", "3.4.5--pyhdfd78af_0": "sha256:13d000bd81346c169a2b387b6d8a038181cb6d5c58c55cde1d9c3528cb13d751", "3.5.0--pyhdfd78af_0": "sha256:3b10a85055a1bc351d4f481c4a93ae04882a3b29e361df7fd0989a30d52ae6dc"}, "docker": "quay.io/biocontainers/drep", "aliases": {"ScaffoldLevel_dRep.py": "/usr/local/bin/ScaffoldLevel_dRep.py", "dRep": "/usr/local/bin/dRep", "delta2vcf": "/usr/local/bin/delta2vcf", "parse_stb.py": "/usr/local/bin/parse_stb.py", "fastANI": "/usr/local/bin/fastANI", "capnp": "/usr/local/bin/capnp", "capnpc": "/usr/local/bin/capnpc", "capnpc-c++": "/usr/local/bin/capnpc-c++", "capnpc-capnp": "/usr/local/bin/capnpc-capnp", "mash": "/usr/local/bin/mash", "combineMUMs": "/usr/local/bin/combineMUMs", "delta-filter": "/usr/local/bin/delta-filter", "dnadiff": "/usr/local/bin/dnadiff", "exact-tandems": "/usr/local/bin/exact-tandems"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/drep.
shpc-registry automated BioContainers addition for drep
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/drep
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/drep:3.5.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/drep/3.5.0--pyhdfd78af_0
$ module help quay.io/biocontainers/drep/3.5.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### drep-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### drep-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### drep-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### drep-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### drep-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### drep-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ScaffoldLevel_dRep.py

```bash
$ singularity exec <container> /usr/local/bin/ScaffoldLevel_dRep.py
$ podman run --it --rm --entrypoint /usr/local/bin/ScaffoldLevel_dRep.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ScaffoldLevel_dRep.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dRep

```bash
$ singularity exec <container> /usr/local/bin/dRep
$ podman run --it --rm --entrypoint /usr/local/bin/dRep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dRep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### delta2vcf

```bash
$ singularity exec <container> /usr/local/bin/delta2vcf
$ podman run --it --rm --entrypoint /usr/local/bin/delta2vcf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/delta2vcf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### parse_stb.py

```bash
$ singularity exec <container> /usr/local/bin/parse_stb.py
$ podman run --it --rm --entrypoint /usr/local/bin/parse_stb.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/parse_stb.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastANI

```bash
$ singularity exec <container> /usr/local/bin/fastANI
$ podman run --it --rm --entrypoint /usr/local/bin/fastANI   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastANI   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### mash

```bash
$ singularity exec <container> /usr/local/bin/mash
$ podman run --it --rm --entrypoint /usr/local/bin/mash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### combineMUMs

```bash
$ singularity exec <container> /usr/local/bin/combineMUMs
$ podman run --it --rm --entrypoint /usr/local/bin/combineMUMs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/combineMUMs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### delta-filter

```bash
$ singularity exec <container> /usr/local/bin/delta-filter
$ podman run --it --rm --entrypoint /usr/local/bin/delta-filter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/delta-filter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dnadiff

```bash
$ singularity exec <container> /usr/local/bin/dnadiff
$ podman run --it --rm --entrypoint /usr/local/bin/dnadiff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dnadiff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### exact-tandems

```bash
$ singularity exec <container> /usr/local/bin/exact-tandems
$ podman run --it --rm --entrypoint /usr/local/bin/exact-tandems   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/exact-tandems   -v ${PWD} -w ${PWD} <container> -c " $@"
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