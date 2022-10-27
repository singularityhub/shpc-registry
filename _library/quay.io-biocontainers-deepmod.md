---
layout: container
name:  "quay.io/biocontainers/deepmod"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/deepmod/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/deepmod/container.yaml"
updated_at: "2022-10-27 00:44:52.587127"
latest: "0.1.3--pyh864c0ab_1"
container_url: "https://biocontainers.pro/tools/deepmod"
aliases:
 - "DeepMod.py"
 - "cal_EcoliDetPerf.py"
 - "generate_motif_pos.py"
 - "hm_cluster_predict.py"
 - "sum_chr_mod.py"
versions:
 - "0.1.3--pyh864c0ab_1"
description: "shpc-registry automated BioContainers addition for deepmod"
config: {"url": "https://biocontainers.pro/tools/deepmod", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for deepmod", "latest": {"0.1.3--pyh864c0ab_1": "sha256:fac869f873415fe71217fa90ba2020d292ec2824ae613f2d013a8f176ad65210"}, "tags": {"0.1.3--pyh864c0ab_1": "sha256:fac869f873415fe71217fa90ba2020d292ec2824ae613f2d013a8f176ad65210"}, "docker": "quay.io/biocontainers/deepmod", "aliases": {"DeepMod.py": "/usr/local/bin/DeepMod.py", "cal_EcoliDetPerf.py": "/usr/local/bin/cal_EcoliDetPerf.py", "generate_motif_pos.py": "/usr/local/bin/generate_motif_pos.py", "hm_cluster_predict.py": "/usr/local/bin/hm_cluster_predict.py", "sum_chr_mod.py": "/usr/local/bin/sum_chr_mod.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/deepmod.
shpc-registry automated BioContainers addition for deepmod
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/deepmod
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/deepmod:0.1.3--pyh864c0ab_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/deepmod/0.1.3--pyh864c0ab_1
$ module help quay.io/biocontainers/deepmod/0.1.3--pyh864c0ab_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### deepmod-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### deepmod-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### deepmod-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### deepmod-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### deepmod-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### deepmod-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### DeepMod.py

```bash
$ singularity exec <container> /usr/local/bin/DeepMod.py
$ podman run --it --rm --entrypoint /usr/local/bin/DeepMod.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/DeepMod.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cal_EcoliDetPerf.py

```bash
$ singularity exec <container> /usr/local/bin/cal_EcoliDetPerf.py
$ podman run --it --rm --entrypoint /usr/local/bin/cal_EcoliDetPerf.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cal_EcoliDetPerf.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### generate_motif_pos.py

```bash
$ singularity exec <container> /usr/local/bin/generate_motif_pos.py
$ podman run --it --rm --entrypoint /usr/local/bin/generate_motif_pos.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/generate_motif_pos.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hm_cluster_predict.py

```bash
$ singularity exec <container> /usr/local/bin/hm_cluster_predict.py
$ podman run --it --rm --entrypoint /usr/local/bin/hm_cluster_predict.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hm_cluster_predict.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sum_chr_mod.py

```bash
$ singularity exec <container> /usr/local/bin/sum_chr_mod.py
$ podman run --it --rm --entrypoint /usr/local/bin/sum_chr_mod.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sum_chr_mod.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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