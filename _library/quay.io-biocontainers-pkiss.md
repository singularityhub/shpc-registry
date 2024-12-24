---
layout: container
name:  "quay.io/biocontainers/pkiss"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pkiss/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pkiss/container.yaml"
updated_at: "2024-12-24 02:58:21.477157"
latest: "2.3.0--pl5321h9948957_3"
container_url: "https://biocontainers.pro/tools/pkiss"
aliases:
 - "addRNAoptions.pl"
 - "gapc"
 - "pKiss"
 - "pKiss_enforce"
 - "pKiss_enforce_window"
 - "pKiss_eval"
 - "pKiss_local"
 - "pKiss_local_window"
 - "pKiss_mfe"
 - "pKiss_mfe_window"
 - "pKiss_probs"
 - "pKiss_probs_window"
 - "pKiss_shapes"
 - "pKiss_shapes_window"
 - "pKiss_subopt"
 - "pKiss_subopt_window"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "2.2.14--pl5321h9f5acd7_2"
 - "2.2.14--pl5321h4ac6f70_3"
 - "2.3.0--pl5321h4ac6f70_2"
 - "2.3.0--pl5321h9948957_3"
description: "shpc-registry automated BioContainers addition for pkiss"
config: {"url": "https://biocontainers.pro/tools/pkiss", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pkiss", "latest": {"2.3.0--pl5321h9948957_3": "sha256:6704acdb447aeb8e931f1a2b1d69482b82f425c7a3fd676f033199d673daf861"}, "tags": {"2.2.14--pl5321h9f5acd7_2": "sha256:cde4ebedc5036c8826220b8dd19453b6579c5121e21dad7852e85f5d60c19b5d", "2.2.14--pl5321h4ac6f70_3": "sha256:f610013c29b1eac00f8c5c5e9d130ccd8d469ebe1001c7176af0db7246694c1f", "2.3.0--pl5321h4ac6f70_2": "sha256:1e164ea3c0f1bf256f265a494c29c45974df5ed7d45cf319e794de06123fc6d9", "2.3.0--pl5321h9948957_3": "sha256:6704acdb447aeb8e931f1a2b1d69482b82f425c7a3fd676f033199d673daf861"}, "docker": "quay.io/biocontainers/pkiss", "aliases": {"addRNAoptions.pl": "/usr/local/bin/addRNAoptions.pl", "gapc": "/usr/local/bin/gapc", "pKiss": "/usr/local/bin/pKiss", "pKiss_enforce": "/usr/local/bin/pKiss_enforce", "pKiss_enforce_window": "/usr/local/bin/pKiss_enforce_window", "pKiss_eval": "/usr/local/bin/pKiss_eval", "pKiss_local": "/usr/local/bin/pKiss_local", "pKiss_local_window": "/usr/local/bin/pKiss_local_window", "pKiss_mfe": "/usr/local/bin/pKiss_mfe", "pKiss_mfe_window": "/usr/local/bin/pKiss_mfe_window", "pKiss_probs": "/usr/local/bin/pKiss_probs", "pKiss_probs_window": "/usr/local/bin/pKiss_probs_window", "pKiss_shapes": "/usr/local/bin/pKiss_shapes", "pKiss_shapes_window": "/usr/local/bin/pKiss_shapes_window", "pKiss_subopt": "/usr/local/bin/pKiss_subopt", "pKiss_subopt_window": "/usr/local/bin/pKiss_subopt_window", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pkiss.
shpc-registry automated BioContainers addition for pkiss
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pkiss
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pkiss:2.3.0--pl5321h9948957_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pkiss/2.3.0--pl5321h9948957_3
$ module help quay.io/biocontainers/pkiss/2.3.0--pl5321h9948957_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pkiss-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pkiss-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pkiss-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pkiss-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pkiss-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pkiss-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### addRNAoptions.pl

```bash
$ singularity exec <container> /usr/local/bin/addRNAoptions.pl
$ podman run --it --rm --entrypoint /usr/local/bin/addRNAoptions.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/addRNAoptions.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gapc

```bash
$ singularity exec <container> /usr/local/bin/gapc
$ podman run --it --rm --entrypoint /usr/local/bin/gapc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gapc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pKiss

```bash
$ singularity exec <container> /usr/local/bin/pKiss
$ podman run --it --rm --entrypoint /usr/local/bin/pKiss   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pKiss   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pKiss_enforce

```bash
$ singularity exec <container> /usr/local/bin/pKiss_enforce
$ podman run --it --rm --entrypoint /usr/local/bin/pKiss_enforce   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pKiss_enforce   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pKiss_enforce_window

```bash
$ singularity exec <container> /usr/local/bin/pKiss_enforce_window
$ podman run --it --rm --entrypoint /usr/local/bin/pKiss_enforce_window   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pKiss_enforce_window   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pKiss_eval

```bash
$ singularity exec <container> /usr/local/bin/pKiss_eval
$ podman run --it --rm --entrypoint /usr/local/bin/pKiss_eval   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pKiss_eval   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pKiss_local

```bash
$ singularity exec <container> /usr/local/bin/pKiss_local
$ podman run --it --rm --entrypoint /usr/local/bin/pKiss_local   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pKiss_local   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pKiss_local_window

```bash
$ singularity exec <container> /usr/local/bin/pKiss_local_window
$ podman run --it --rm --entrypoint /usr/local/bin/pKiss_local_window   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pKiss_local_window   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pKiss_mfe

```bash
$ singularity exec <container> /usr/local/bin/pKiss_mfe
$ podman run --it --rm --entrypoint /usr/local/bin/pKiss_mfe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pKiss_mfe   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pKiss_mfe_window

```bash
$ singularity exec <container> /usr/local/bin/pKiss_mfe_window
$ podman run --it --rm --entrypoint /usr/local/bin/pKiss_mfe_window   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pKiss_mfe_window   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pKiss_probs

```bash
$ singularity exec <container> /usr/local/bin/pKiss_probs
$ podman run --it --rm --entrypoint /usr/local/bin/pKiss_probs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pKiss_probs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pKiss_probs_window

```bash
$ singularity exec <container> /usr/local/bin/pKiss_probs_window
$ podman run --it --rm --entrypoint /usr/local/bin/pKiss_probs_window   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pKiss_probs_window   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pKiss_shapes

```bash
$ singularity exec <container> /usr/local/bin/pKiss_shapes
$ podman run --it --rm --entrypoint /usr/local/bin/pKiss_shapes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pKiss_shapes   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pKiss_shapes_window

```bash
$ singularity exec <container> /usr/local/bin/pKiss_shapes_window
$ podman run --it --rm --entrypoint /usr/local/bin/pKiss_shapes_window   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pKiss_shapes_window   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pKiss_subopt

```bash
$ singularity exec <container> /usr/local/bin/pKiss_subopt
$ podman run --it --rm --entrypoint /usr/local/bin/pKiss_subopt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pKiss_subopt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pKiss_subopt_window

```bash
$ singularity exec <container> /usr/local/bin/pKiss_subopt_window
$ podman run --it --rm --entrypoint /usr/local/bin/pKiss_subopt_window   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pKiss_subopt_window   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perl5.32.1

```bash
$ singularity exec <container> /usr/local/bin/perl5.32.1
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.32.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.32.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### streamzip

```bash
$ singularity exec <container> /usr/local/bin/streamzip
$ podman run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
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