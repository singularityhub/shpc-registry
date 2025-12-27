---
layout: container
name:  "quay.io/biocontainers/palikiss"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/palikiss/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/palikiss/container.yaml"
updated_at: "2025-12-27 03:45:40.401586"
latest: "1.1.0--pl5321h9948957_2"
container_url: "https://biocontainers.pro/tools/palikiss"
aliases:
 - "addRNAoptions.pl"
 - "gapc"
 - "pAliKiss"
 - "pAliKiss_enforce"
 - "pAliKiss_enforce_window"
 - "pAliKiss_eval"
 - "pAliKiss_local"
 - "pAliKiss_local_window"
 - "pAliKiss_mfe"
 - "pAliKiss_mfe_window"
 - "pAliKiss_probs"
 - "pAliKiss_probs_window"
 - "pAliKiss_rep_consensus"
 - "pAliKiss_rep_mis"
 - "pAliKiss_sci"
 - "pAliKiss_shapes"
 - "pAliKiss_shapes_window"
 - "pAliKiss_subopt"
 - "pAliKiss_subopt_window"
versions:
 - "1.1.0--pl5321h4ac6f70_0"
 - "1.1.0--pl5321h4ac6f70_1"
 - "1.1.0--pl5321h9948957_2"
description: "singularity registry hpc automated addition for palikiss"
config: {"url": "https://biocontainers.pro/tools/palikiss", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for palikiss", "latest": {"1.1.0--pl5321h9948957_2": "sha256:23235d32b47bc04ffe1afc990460f1233f7ee91a8cf1dd953d24badde6cd5d3f"}, "tags": {"1.1.0--pl5321h4ac6f70_0": "sha256:136f308f3bb9662125d16c4c03aea04946e0a78a4d08fe34b2e2b91507524c45", "1.1.0--pl5321h4ac6f70_1": "sha256:d60da4d386f30d9fb19cfc2ef6b6a6322b937eca28210eac411a3dee35d02946", "1.1.0--pl5321h9948957_2": "sha256:23235d32b47bc04ffe1afc990460f1233f7ee91a8cf1dd953d24badde6cd5d3f"}, "docker": "quay.io/biocontainers/palikiss", "aliases": {"addRNAoptions.pl": "/usr/local/bin/addRNAoptions.pl", "gapc": "/usr/local/bin/gapc", "pAliKiss": "/usr/local/bin/pAliKiss", "pAliKiss_enforce": "/usr/local/bin/pAliKiss_enforce", "pAliKiss_enforce_window": "/usr/local/bin/pAliKiss_enforce_window", "pAliKiss_eval": "/usr/local/bin/pAliKiss_eval", "pAliKiss_local": "/usr/local/bin/pAliKiss_local", "pAliKiss_local_window": "/usr/local/bin/pAliKiss_local_window", "pAliKiss_mfe": "/usr/local/bin/pAliKiss_mfe", "pAliKiss_mfe_window": "/usr/local/bin/pAliKiss_mfe_window", "pAliKiss_probs": "/usr/local/bin/pAliKiss_probs", "pAliKiss_probs_window": "/usr/local/bin/pAliKiss_probs_window", "pAliKiss_rep_consensus": "/usr/local/bin/pAliKiss_rep_consensus", "pAliKiss_rep_mis": "/usr/local/bin/pAliKiss_rep_mis", "pAliKiss_sci": "/usr/local/bin/pAliKiss_sci", "pAliKiss_shapes": "/usr/local/bin/pAliKiss_shapes", "pAliKiss_shapes_window": "/usr/local/bin/pAliKiss_shapes_window", "pAliKiss_subopt": "/usr/local/bin/pAliKiss_subopt", "pAliKiss_subopt_window": "/usr/local/bin/pAliKiss_subopt_window"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/palikiss.
singularity registry hpc automated addition for palikiss
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/palikiss
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/palikiss:1.1.0--pl5321h9948957_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/palikiss/1.1.0--pl5321h9948957_2
$ module help quay.io/biocontainers/palikiss/1.1.0--pl5321h9948957_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### palikiss-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### palikiss-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### palikiss-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### palikiss-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### palikiss-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### palikiss-inspect-deffile:

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


#### pAliKiss

```bash
$ singularity exec <container> /usr/local/bin/pAliKiss
$ podman run --it --rm --entrypoint /usr/local/bin/pAliKiss   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pAliKiss   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pAliKiss_enforce

```bash
$ singularity exec <container> /usr/local/bin/pAliKiss_enforce
$ podman run --it --rm --entrypoint /usr/local/bin/pAliKiss_enforce   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pAliKiss_enforce   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pAliKiss_enforce_window

```bash
$ singularity exec <container> /usr/local/bin/pAliKiss_enforce_window
$ podman run --it --rm --entrypoint /usr/local/bin/pAliKiss_enforce_window   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pAliKiss_enforce_window   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pAliKiss_eval

```bash
$ singularity exec <container> /usr/local/bin/pAliKiss_eval
$ podman run --it --rm --entrypoint /usr/local/bin/pAliKiss_eval   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pAliKiss_eval   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pAliKiss_local

```bash
$ singularity exec <container> /usr/local/bin/pAliKiss_local
$ podman run --it --rm --entrypoint /usr/local/bin/pAliKiss_local   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pAliKiss_local   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pAliKiss_local_window

```bash
$ singularity exec <container> /usr/local/bin/pAliKiss_local_window
$ podman run --it --rm --entrypoint /usr/local/bin/pAliKiss_local_window   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pAliKiss_local_window   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pAliKiss_mfe

```bash
$ singularity exec <container> /usr/local/bin/pAliKiss_mfe
$ podman run --it --rm --entrypoint /usr/local/bin/pAliKiss_mfe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pAliKiss_mfe   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pAliKiss_mfe_window

```bash
$ singularity exec <container> /usr/local/bin/pAliKiss_mfe_window
$ podman run --it --rm --entrypoint /usr/local/bin/pAliKiss_mfe_window   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pAliKiss_mfe_window   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pAliKiss_probs

```bash
$ singularity exec <container> /usr/local/bin/pAliKiss_probs
$ podman run --it --rm --entrypoint /usr/local/bin/pAliKiss_probs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pAliKiss_probs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pAliKiss_probs_window

```bash
$ singularity exec <container> /usr/local/bin/pAliKiss_probs_window
$ podman run --it --rm --entrypoint /usr/local/bin/pAliKiss_probs_window   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pAliKiss_probs_window   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pAliKiss_rep_consensus

```bash
$ singularity exec <container> /usr/local/bin/pAliKiss_rep_consensus
$ podman run --it --rm --entrypoint /usr/local/bin/pAliKiss_rep_consensus   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pAliKiss_rep_consensus   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pAliKiss_rep_mis

```bash
$ singularity exec <container> /usr/local/bin/pAliKiss_rep_mis
$ podman run --it --rm --entrypoint /usr/local/bin/pAliKiss_rep_mis   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pAliKiss_rep_mis   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pAliKiss_sci

```bash
$ singularity exec <container> /usr/local/bin/pAliKiss_sci
$ podman run --it --rm --entrypoint /usr/local/bin/pAliKiss_sci   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pAliKiss_sci   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pAliKiss_shapes

```bash
$ singularity exec <container> /usr/local/bin/pAliKiss_shapes
$ podman run --it --rm --entrypoint /usr/local/bin/pAliKiss_shapes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pAliKiss_shapes   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pAliKiss_shapes_window

```bash
$ singularity exec <container> /usr/local/bin/pAliKiss_shapes_window
$ podman run --it --rm --entrypoint /usr/local/bin/pAliKiss_shapes_window   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pAliKiss_shapes_window   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pAliKiss_subopt

```bash
$ singularity exec <container> /usr/local/bin/pAliKiss_subopt
$ podman run --it --rm --entrypoint /usr/local/bin/pAliKiss_subopt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pAliKiss_subopt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pAliKiss_subopt_window

```bash
$ singularity exec <container> /usr/local/bin/pAliKiss_subopt_window
$ podman run --it --rm --entrypoint /usr/local/bin/pAliKiss_subopt_window   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pAliKiss_subopt_window   -v ${PWD} -w ${PWD} <container> -c " $@"
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