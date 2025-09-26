---
layout: container
name:  "quay.io/biocontainers/sistr_cmd"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sistr_cmd/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/sistr_cmd/container.yaml"
updated_at: "2025-09-26 03:17:21.424784"
latest: "1.1.3--pyhdc42f0e_2"
container_url: "https://biocontainers.pro/tools/sistr_cmd"
aliases:
 - "sistr"
 - "test_pcre"
 - "capnp"
 - "capnpc"
 - "capnpc-c++"
 - "capnpc-capnp"
 - "mash"
 - "blastdbcp"
 - "gene_info_reader"
 - "seqdb_demo"
 - "seqdb_perf"
versions:
 - "1.1.1--pyh864c0ab_2"
 - "1.1.1--pyh7cba7a3_3"
 - "1.1.2--pyhca03a8a_0"
 - "1.1.2--pyhca03a8a_1"
 - "1.1.3--pyhdc42f0e_0"
 - "1.1.3--pyhdc42f0e_1"
 - "1.1.3--pyhdc42f0e_2"
description: "shpc-registry automated BioContainers addition for sistr_cmd"
config: {"url": "https://biocontainers.pro/tools/sistr_cmd", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for sistr_cmd", "latest": {"1.1.3--pyhdc42f0e_2": "sha256:91619cb8daecadeeb457f56e38bd6e5ec980d76e521067eccf1355984bfd4171"}, "tags": {"1.1.1--pyh864c0ab_2": "sha256:0068bd3708615599f2ed4229338a9aa59cd2cc43a66c199d931da0d51261f211", "1.1.1--pyh7cba7a3_3": "sha256:b50e23909bb7b68823785fe7d4fb76c29c24d2ea542d998d8a3d93f24bfd6f16", "1.1.2--pyhca03a8a_0": "sha256:c7b064f018e1e56934fb45c0525e6eaac953384ac01c0422d2dee749dddbadf3", "1.1.2--pyhca03a8a_1": "sha256:477fd987588170d7215e78abe2351a57a004273204153f6ceb9c32149971c5ad", "1.1.3--pyhdc42f0e_0": "sha256:93c6b6c9ea09c874408295f23604f7f14a89d94cc4418d2181d5cb19f0edcd7f", "1.1.3--pyhdc42f0e_1": "sha256:d3d7f9cf4604a5f527edccada7f25a901568e174e8a864f88fad181549b53faf", "1.1.3--pyhdc42f0e_2": "sha256:91619cb8daecadeeb457f56e38bd6e5ec980d76e521067eccf1355984bfd4171"}, "docker": "quay.io/biocontainers/sistr_cmd", "aliases": {"sistr": "/usr/local/bin/sistr", "test_pcre": "/usr/local/bin/test_pcre", "capnp": "/usr/local/bin/capnp", "capnpc": "/usr/local/bin/capnpc", "capnpc-c++": "/usr/local/bin/capnpc-c++", "capnpc-capnp": "/usr/local/bin/capnpc-capnp", "mash": "/usr/local/bin/mash", "blastdbcp": "/usr/local/bin/blastdbcp", "gene_info_reader": "/usr/local/bin/gene_info_reader", "seqdb_demo": "/usr/local/bin/seqdb_demo", "seqdb_perf": "/usr/local/bin/seqdb_perf"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/sistr_cmd.
shpc-registry automated BioContainers addition for sistr_cmd
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sistr_cmd
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sistr_cmd:1.1.3--pyhdc42f0e_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sistr_cmd/1.1.3--pyhdc42f0e_2
$ module help quay.io/biocontainers/sistr_cmd/1.1.3--pyhdc42f0e_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sistr_cmd-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sistr_cmd-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sistr_cmd-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sistr_cmd-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sistr_cmd-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sistr_cmd-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### sistr

```bash
$ singularity exec <container> /usr/local/bin/sistr
$ podman run --it --rm --entrypoint /usr/local/bin/sistr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sistr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### test_pcre

```bash
$ singularity exec <container> /usr/local/bin/test_pcre
$ podman run --it --rm --entrypoint /usr/local/bin/test_pcre   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/test_pcre   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### blastdbcp

```bash
$ singularity exec <container> /usr/local/bin/blastdbcp
$ podman run --it --rm --entrypoint /usr/local/bin/blastdbcp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastdbcp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gene_info_reader

```bash
$ singularity exec <container> /usr/local/bin/gene_info_reader
$ podman run --it --rm --entrypoint /usr/local/bin/gene_info_reader   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gene_info_reader   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seqdb_demo

```bash
$ singularity exec <container> /usr/local/bin/seqdb_demo
$ podman run --it --rm --entrypoint /usr/local/bin/seqdb_demo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seqdb_demo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seqdb_perf

```bash
$ singularity exec <container> /usr/local/bin/seqdb_perf
$ podman run --it --rm --entrypoint /usr/local/bin/seqdb_perf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seqdb_perf   -v ${PWD} -w ${PWD} <container> -c " $@"
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