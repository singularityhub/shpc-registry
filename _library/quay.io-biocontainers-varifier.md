---
layout: container
name:  "quay.io/biocontainers/varifier"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/varifier/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/varifier/container.yaml"
updated_at: "2023-04-22 02:49:22.026144"
latest: "0.3.1--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/varifier"
aliases:
 - "delta2vcf"
 - "varifier"
 - "vt"
 - "tabix++"
 - "minimap2.py"
 - "plotBfst.R"
 - "plotHapLrt.R"
 - "plotHaplotypes.R"
 - "plotPfst.R"
 - "plotSmoothed.R"
 - "plotWCfst.R"
 - "plotXPEHH.R"
versions:
 - "0.3.1--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for varifier"
config: {"url": "https://biocontainers.pro/tools/varifier", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for varifier", "latest": {"0.3.1--pyhdfd78af_0": "sha256:ad822cf6f08e12986c5bc1a7d2819695728a6ddd749ccb76ad34f202a52bf669"}, "tags": {"0.3.1--pyhdfd78af_0": "sha256:ad822cf6f08e12986c5bc1a7d2819695728a6ddd749ccb76ad34f202a52bf669"}, "docker": "quay.io/biocontainers/varifier", "aliases": {"delta2vcf": "/usr/local/bin/delta2vcf", "varifier": "/usr/local/bin/varifier", "vt": "/usr/local/bin/vt", "tabix++": "/usr/local/bin/tabix++", "minimap2.py": "/usr/local/bin/minimap2.py", "plotBfst.R": "/usr/local/bin/plotBfst.R", "plotHapLrt.R": "/usr/local/bin/plotHapLrt.R", "plotHaplotypes.R": "/usr/local/bin/plotHaplotypes.R", "plotPfst.R": "/usr/local/bin/plotPfst.R", "plotSmoothed.R": "/usr/local/bin/plotSmoothed.R", "plotWCfst.R": "/usr/local/bin/plotWCfst.R", "plotXPEHH.R": "/usr/local/bin/plotXPEHH.R"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/varifier.
shpc-registry automated BioContainers addition for varifier
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/varifier
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/varifier:0.3.1--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/varifier/0.3.1--pyhdfd78af_0
$ module help quay.io/biocontainers/varifier/0.3.1--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### varifier-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### varifier-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### varifier-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### varifier-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### varifier-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### varifier-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### delta2vcf

```bash
$ singularity exec <container> /usr/local/bin/delta2vcf
$ podman run --it --rm --entrypoint /usr/local/bin/delta2vcf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/delta2vcf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### varifier

```bash
$ singularity exec <container> /usr/local/bin/varifier
$ podman run --it --rm --entrypoint /usr/local/bin/varifier   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/varifier   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vt

```bash
$ singularity exec <container> /usr/local/bin/vt
$ podman run --it --rm --entrypoint /usr/local/bin/vt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tabix++

```bash
$ singularity exec <container> /usr/local/bin/tabix++
$ podman run --it --rm --entrypoint /usr/local/bin/tabix++   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tabix++   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### minimap2.py

```bash
$ singularity exec <container> /usr/local/bin/minimap2.py
$ podman run --it --rm --entrypoint /usr/local/bin/minimap2.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/minimap2.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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