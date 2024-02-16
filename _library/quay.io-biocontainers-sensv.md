---
layout: container
name:  "quay.io/biocontainers/sensv"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sensv/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/sensv/container.yaml"
updated_at: "2024-02-16 02:48:14.351469"
latest: "1.0.4--h43eeafb_2"
container_url: "https://biocontainers.pro/tools/sensv"
aliases:
 - "Makefile"
 - "SURVIVOR"
 - "config.ini"
 - "grabix"
 - "pypy3"
 - "sensv"
 - "vcfnormalizesvs"
 - "vcfnull2ref"
 - "vcfunphase"
 - "gdbm_dump"
 - "gdbm_load"
 - "gdbmtool"
 - "plotBfst.R"
 - "plotHapLrt.R"
 - "plotHaplotypes.R"
 - "plotPfst.R"
 - "plotSmoothed.R"
 - "plotWCfst.R"
 - "plotXPEHH.R"
versions:
 - "v1.0.1--h8b12597_0"
 - "1.0.4--h5b5514e_1"
 - "1.0.4--h43eeafb_2"
description: "shpc-registry automated BioContainers addition for sensv"
config: {"url": "https://biocontainers.pro/tools/sensv", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for sensv", "latest": {"1.0.4--h43eeafb_2": "sha256:9bc27ada3af9f71e572559275ae7e3d3411985e3149973f85cbba2fe33cbdfdf"}, "tags": {"v1.0.1--h8b12597_0": "sha256:001423fe13c250b9d74dcdca4043a55e6e654f5326b93ed5ced03514d3b85d5b", "1.0.4--h5b5514e_1": "sha256:89efedfdcac3e246e2cefb5860ae78a8d21dc72d2581d5b9bde22adf0b2cd301", "1.0.4--h43eeafb_2": "sha256:9bc27ada3af9f71e572559275ae7e3d3411985e3149973f85cbba2fe33cbdfdf"}, "docker": "quay.io/biocontainers/sensv", "aliases": {"Makefile": "/usr/local/bin/Makefile", "SURVIVOR": "/usr/local/bin/SURVIVOR", "config.ini": "/usr/local/bin/config.ini", "grabix": "/usr/local/bin/grabix", "pypy3": "/usr/local/bin/pypy3", "sensv": "/usr/local/bin/sensv", "vcfnormalizesvs": "/usr/local/bin/vcfnormalizesvs", "vcfnull2ref": "/usr/local/bin/vcfnull2ref", "vcfunphase": "/usr/local/bin/vcfunphase", "gdbm_dump": "/usr/local/bin/gdbm_dump", "gdbm_load": "/usr/local/bin/gdbm_load", "gdbmtool": "/usr/local/bin/gdbmtool", "plotBfst.R": "/usr/local/bin/plotBfst.R", "plotHapLrt.R": "/usr/local/bin/plotHapLrt.R", "plotHaplotypes.R": "/usr/local/bin/plotHaplotypes.R", "plotPfst.R": "/usr/local/bin/plotPfst.R", "plotSmoothed.R": "/usr/local/bin/plotSmoothed.R", "plotWCfst.R": "/usr/local/bin/plotWCfst.R", "plotXPEHH.R": "/usr/local/bin/plotXPEHH.R"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/sensv.
shpc-registry automated BioContainers addition for sensv
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sensv
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sensv:1.0.4--h43eeafb_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sensv/1.0.4--h43eeafb_2
$ module help quay.io/biocontainers/sensv/1.0.4--h43eeafb_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sensv-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sensv-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sensv-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sensv-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sensv-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sensv-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Makefile

```bash
$ singularity exec <container> /usr/local/bin/Makefile
$ podman run --it --rm --entrypoint /usr/local/bin/Makefile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Makefile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SURVIVOR

```bash
$ singularity exec <container> /usr/local/bin/SURVIVOR
$ podman run --it --rm --entrypoint /usr/local/bin/SURVIVOR   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SURVIVOR   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### config.ini

```bash
$ singularity exec <container> /usr/local/bin/config.ini
$ podman run --it --rm --entrypoint /usr/local/bin/config.ini   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/config.ini   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grabix

```bash
$ singularity exec <container> /usr/local/bin/grabix
$ podman run --it --rm --entrypoint /usr/local/bin/grabix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grabix   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pypy3

```bash
$ singularity exec <container> /usr/local/bin/pypy3
$ podman run --it --rm --entrypoint /usr/local/bin/pypy3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pypy3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sensv

```bash
$ singularity exec <container> /usr/local/bin/sensv
$ podman run --it --rm --entrypoint /usr/local/bin/sensv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sensv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcfnormalizesvs

```bash
$ singularity exec <container> /usr/local/bin/vcfnormalizesvs
$ podman run --it --rm --entrypoint /usr/local/bin/vcfnormalizesvs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcfnormalizesvs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcfnull2ref

```bash
$ singularity exec <container> /usr/local/bin/vcfnull2ref
$ podman run --it --rm --entrypoint /usr/local/bin/vcfnull2ref   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcfnull2ref   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcfunphase

```bash
$ singularity exec <container> /usr/local/bin/vcfunphase
$ podman run --it --rm --entrypoint /usr/local/bin/vcfunphase   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcfunphase   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdbm_dump

```bash
$ singularity exec <container> /usr/local/bin/gdbm_dump
$ podman run --it --rm --entrypoint /usr/local/bin/gdbm_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdbm_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdbm_load

```bash
$ singularity exec <container> /usr/local/bin/gdbm_load
$ podman run --it --rm --entrypoint /usr/local/bin/gdbm_load   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdbm_load   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdbmtool

```bash
$ singularity exec <container> /usr/local/bin/gdbmtool
$ podman run --it --rm --entrypoint /usr/local/bin/gdbmtool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdbmtool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plotBfst.R

```bash
$ singularity exec <container> /usr/local/bin/plotBfst.R
$ podman run --it --rm --entrypoint /usr/local/bin/plotBfst.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plotBfst.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plotHapLrt.R

```bash
$ singularity exec <container> /usr/local/bin/plotHapLrt.R
$ podman run --it --rm --entrypoint /usr/local/bin/plotHapLrt.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plotHapLrt.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plotHaplotypes.R

```bash
$ singularity exec <container> /usr/local/bin/plotHaplotypes.R
$ podman run --it --rm --entrypoint /usr/local/bin/plotHaplotypes.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plotHaplotypes.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plotPfst.R

```bash
$ singularity exec <container> /usr/local/bin/plotPfst.R
$ podman run --it --rm --entrypoint /usr/local/bin/plotPfst.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plotPfst.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plotSmoothed.R

```bash
$ singularity exec <container> /usr/local/bin/plotSmoothed.R
$ podman run --it --rm --entrypoint /usr/local/bin/plotSmoothed.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plotSmoothed.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plotWCfst.R

```bash
$ singularity exec <container> /usr/local/bin/plotWCfst.R
$ podman run --it --rm --entrypoint /usr/local/bin/plotWCfst.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plotWCfst.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plotXPEHH.R

```bash
$ singularity exec <container> /usr/local/bin/plotXPEHH.R
$ podman run --it --rm --entrypoint /usr/local/bin/plotXPEHH.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plotXPEHH.R   -v ${PWD} -w ${PWD} <container> -c " $@"
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