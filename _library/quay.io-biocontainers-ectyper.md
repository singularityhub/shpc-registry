---
layout: container
name:  "quay.io/biocontainers/ectyper"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ectyper/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ectyper/container.yaml"
updated_at: "2025-12-19 03:38:33.939199"
latest: "2.0.0--pyhdfd78af_4"
container_url: "https://biocontainers.pro/tools/ectyper"
aliases:
 - "ectyper"
 - "capnp"
 - "capnpc"
 - "capnpc-c++"
 - "capnpc-capnp"
 - "gff2gff.py"
 - "mash"
 - "seqtk"
 - "CA.pm"
 - "cacert.pem"
 - "index-themes"
versions:
 - "1.0.0--pyhdfd78af_1"
 - "2.0.0--pyhdfd78af_1"
 - "2.0.0--pyhdfd78af_2"
 - "2.0.0--pyhdfd78af_3"
 - "2.0.0--pyhdfd78af_4"
description: "shpc-registry automated BioContainers addition for ectyper"
config: {"url": "https://biocontainers.pro/tools/ectyper", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ectyper", "latest": {"2.0.0--pyhdfd78af_4": "sha256:eb98dad0da8a8dbf8864ab724aa51bd59db1a5a80705cadb9c6e0a834ab4ba85"}, "tags": {"1.0.0--pyhdfd78af_1": "sha256:6a9bde6f67c77754bc535211913196165b6c458c3813eed5c3dbfee5165c4465", "2.0.0--pyhdfd78af_1": "sha256:2e37d012760687ca305001706211c693c857135c9f3266a98970f9cf68644bf2", "2.0.0--pyhdfd78af_2": "sha256:1b33a7eb198b1557cff3f03faf0cecb24b5eb5538995e651986e15940c04cc4d", "2.0.0--pyhdfd78af_3": "sha256:7e55de9fab17d114ff087ce4054a9c3a2eca7fd0541b80817b2fc478b71c9503", "2.0.0--pyhdfd78af_4": "sha256:eb98dad0da8a8dbf8864ab724aa51bd59db1a5a80705cadb9c6e0a834ab4ba85"}, "docker": "quay.io/biocontainers/ectyper", "aliases": {"ectyper": "/usr/local/bin/ectyper", "capnp": "/usr/local/bin/capnp", "capnpc": "/usr/local/bin/capnpc", "capnpc-c++": "/usr/local/bin/capnpc-c++", "capnpc-capnp": "/usr/local/bin/capnpc-capnp", "gff2gff.py": "/usr/local/bin/gff2gff.py", "mash": "/usr/local/bin/mash", "seqtk": "/usr/local/bin/seqtk", "CA.pm": "/usr/local/bin/CA.pm", "cacert.pem": "/usr/local/bin/cacert.pem", "index-themes": "/usr/local/bin/index-themes"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ectyper.
shpc-registry automated BioContainers addition for ectyper
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ectyper
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ectyper:2.0.0--pyhdfd78af_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ectyper/2.0.0--pyhdfd78af_4
$ module help quay.io/biocontainers/ectyper/2.0.0--pyhdfd78af_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ectyper-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ectyper-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ectyper-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ectyper-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ectyper-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ectyper-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ectyper

```bash
$ singularity exec <container> /usr/local/bin/ectyper
$ podman run --it --rm --entrypoint /usr/local/bin/ectyper   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ectyper   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### gff2gff.py

```bash
$ singularity exec <container> /usr/local/bin/gff2gff.py
$ podman run --it --rm --entrypoint /usr/local/bin/gff2gff.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff2gff.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mash

```bash
$ singularity exec <container> /usr/local/bin/mash
$ podman run --it --rm --entrypoint /usr/local/bin/mash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seqtk

```bash
$ singularity exec <container> /usr/local/bin/seqtk
$ podman run --it --rm --entrypoint /usr/local/bin/seqtk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seqtk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CA.pm

```bash
$ singularity exec <container> /usr/local/bin/CA.pm
$ podman run --it --rm --entrypoint /usr/local/bin/CA.pm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CA.pm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cacert.pem

```bash
$ singularity exec <container> /usr/local/bin/cacert.pem
$ podman run --it --rm --entrypoint /usr/local/bin/cacert.pem   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cacert.pem   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### index-themes

```bash
$ singularity exec <container> /usr/local/bin/index-themes
$ podman run --it --rm --entrypoint /usr/local/bin/index-themes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/index-themes   -v ${PWD} -w ${PWD} <container> -c " $@"
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