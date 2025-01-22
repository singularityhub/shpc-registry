---
layout: container
name:  "quay.io/biocontainers/instrain"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/instrain/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/instrain/container.yaml"
updated_at: "2025-01-22 03:24:24.529084"
latest: "1.9.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/instrain"
aliases:
 - "ScaffoldLevel_dRep.py"
 - "dRep"
 - "delta2vcf"
 - "inStrain"
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
 - "1.6.3--pyhdfd78af_0"
 - "1.6.4--pyhdfd78af_0"
 - "1.7.1--pyhdfd78af_1"
 - "1.7.5--pyhdfd78af_0"
 - "1.7.6--pyhdfd78af_0"
 - "1.8.0--pyhdfd78af_0"
 - "1.9.0--pyhdfd78af_0"
 - "1.8.1--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for instrain"
config: {"url": "https://biocontainers.pro/tools/instrain", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for instrain", "latest": {"1.9.0--pyhdfd78af_0": "sha256:85b04905a63383f0674e54faba2583a4a107ee9714f37a06a468a492d1dca595"}, "tags": {"1.6.3--pyhdfd78af_0": "sha256:d5eee857a567b91b778ca593c69ae410fcd804b668dbeaa703f4b0f99232e88a", "1.6.4--pyhdfd78af_0": "sha256:539ddd8ed942f7bcc97e20d471e615d0f9a74dcf23710f9bc7c3704136b09849", "1.7.1--pyhdfd78af_1": "sha256:b3a669afd0c9933d30e11c019398c75c9cea45431f03f879d040966f60002848", "1.7.5--pyhdfd78af_0": "sha256:5a7b2b179b746f9b00f965a04f1fada366a9c57eacff99154d0808256cb6be3f", "1.7.6--pyhdfd78af_0": "sha256:7ef1f4de876ab50a0022e492889e0bbfae97d3c8edd67c06cc8c7ebe9976474d", "1.8.0--pyhdfd78af_0": "sha256:c0ae29f1b57837947b420461c93b370064a41aea380f8fdf58140b5d12ea9262", "1.9.0--pyhdfd78af_0": "sha256:85b04905a63383f0674e54faba2583a4a107ee9714f37a06a468a492d1dca595", "1.8.1--pyhdfd78af_0": "sha256:ff92b5e0ec1662085ddf3d9eec0bfe48db400818dff19357a290d617530bce6d"}, "docker": "quay.io/biocontainers/instrain", "aliases": {"ScaffoldLevel_dRep.py": "/usr/local/bin/ScaffoldLevel_dRep.py", "dRep": "/usr/local/bin/dRep", "delta2vcf": "/usr/local/bin/delta2vcf", "inStrain": "/usr/local/bin/inStrain", "parse_stb.py": "/usr/local/bin/parse_stb.py", "fastANI": "/usr/local/bin/fastANI", "capnp": "/usr/local/bin/capnp", "capnpc": "/usr/local/bin/capnpc", "capnpc-c++": "/usr/local/bin/capnpc-c++", "capnpc-capnp": "/usr/local/bin/capnpc-capnp", "mash": "/usr/local/bin/mash", "combineMUMs": "/usr/local/bin/combineMUMs", "delta-filter": "/usr/local/bin/delta-filter", "dnadiff": "/usr/local/bin/dnadiff", "exact-tandems": "/usr/local/bin/exact-tandems"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/instrain.
shpc-registry automated BioContainers addition for instrain
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/instrain
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/instrain:1.9.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/instrain/1.9.0--pyhdfd78af_0
$ module help quay.io/biocontainers/instrain/1.9.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### instrain-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### instrain-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### instrain-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### instrain-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### instrain-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### instrain-inspect-deffile:

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


#### inStrain

```bash
$ singularity exec <container> /usr/local/bin/inStrain
$ podman run --it --rm --entrypoint /usr/local/bin/inStrain   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/inStrain   -v ${PWD} -w ${PWD} <container> -c " $@"
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