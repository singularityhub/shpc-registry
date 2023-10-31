---
layout: container
name:  "quay.io/biocontainers/ribocode"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ribocode/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ribocode/container.yaml"
updated_at: "2023-10-31 02:53:44.036037"
latest: "1.2.15--pyhfa5458b_0"
container_url: "https://biocontainers.pro/tools/ribocode"
aliases:
 - "GTFupdate"
 - "ORFcount"
 - "RiboCode"
 - "RiboCode_onestep"
 - "metaplots"
 - "plot_orf_density"
 - "prepare_transcripts"
 - "pyfasta"
 - "createfontdatachunk.py"
 - "htseq-count"
 - "htseq-qa"
 - "enhancer.py"
 - "explode.py"
 - "gifmaker.py"
 - "painter.py"
 - "player.py"
 - "thresholder.py"
 - "viewer.py"
versions:
 - "1.2.9--py36_0"
 - "1.2.15--pyhfa5458b_0"
description: "shpc-registry automated BioContainers addition for ribocode"
config: {"url": "https://biocontainers.pro/tools/ribocode", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ribocode", "latest": {"1.2.15--pyhfa5458b_0": "sha256:639d557367b237bd2bfac63f94fed0a47bb952e0de9068140583651fa8d1b195"}, "tags": {"1.2.9--py36_0": "sha256:3b319abf8e7e774c1eb51a423834f5abd099704f56e94d02acb8e8b89e4bd3dc", "1.2.15--pyhfa5458b_0": "sha256:639d557367b237bd2bfac63f94fed0a47bb952e0de9068140583651fa8d1b195"}, "docker": "quay.io/biocontainers/ribocode", "aliases": {"GTFupdate": "/usr/local/bin/GTFupdate", "ORFcount": "/usr/local/bin/ORFcount", "RiboCode": "/usr/local/bin/RiboCode", "RiboCode_onestep": "/usr/local/bin/RiboCode_onestep", "metaplots": "/usr/local/bin/metaplots", "plot_orf_density": "/usr/local/bin/plot_orf_density", "prepare_transcripts": "/usr/local/bin/prepare_transcripts", "pyfasta": "/usr/local/bin/pyfasta", "createfontdatachunk.py": "/usr/local/bin/createfontdatachunk.py", "htseq-count": "/usr/local/bin/htseq-count", "htseq-qa": "/usr/local/bin/htseq-qa", "enhancer.py": "/usr/local/bin/enhancer.py", "explode.py": "/usr/local/bin/explode.py", "gifmaker.py": "/usr/local/bin/gifmaker.py", "painter.py": "/usr/local/bin/painter.py", "player.py": "/usr/local/bin/player.py", "thresholder.py": "/usr/local/bin/thresholder.py", "viewer.py": "/usr/local/bin/viewer.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ribocode.
shpc-registry automated BioContainers addition for ribocode
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ribocode
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ribocode:1.2.15--pyhfa5458b_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ribocode/1.2.15--pyhfa5458b_0
$ module help quay.io/biocontainers/ribocode/1.2.15--pyhfa5458b_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ribocode-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ribocode-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ribocode-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ribocode-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ribocode-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ribocode-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### GTFupdate

```bash
$ singularity exec <container> /usr/local/bin/GTFupdate
$ podman run --it --rm --entrypoint /usr/local/bin/GTFupdate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GTFupdate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ORFcount

```bash
$ singularity exec <container> /usr/local/bin/ORFcount
$ podman run --it --rm --entrypoint /usr/local/bin/ORFcount   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ORFcount   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RiboCode

```bash
$ singularity exec <container> /usr/local/bin/RiboCode
$ podman run --it --rm --entrypoint /usr/local/bin/RiboCode   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RiboCode   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RiboCode_onestep

```bash
$ singularity exec <container> /usr/local/bin/RiboCode_onestep
$ podman run --it --rm --entrypoint /usr/local/bin/RiboCode_onestep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RiboCode_onestep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaplots

```bash
$ singularity exec <container> /usr/local/bin/metaplots
$ podman run --it --rm --entrypoint /usr/local/bin/metaplots   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaplots   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plot_orf_density

```bash
$ singularity exec <container> /usr/local/bin/plot_orf_density
$ podman run --it --rm --entrypoint /usr/local/bin/plot_orf_density   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot_orf_density   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prepare_transcripts

```bash
$ singularity exec <container> /usr/local/bin/prepare_transcripts
$ podman run --it --rm --entrypoint /usr/local/bin/prepare_transcripts   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prepare_transcripts   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyfasta

```bash
$ singularity exec <container> /usr/local/bin/pyfasta
$ podman run --it --rm --entrypoint /usr/local/bin/pyfasta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyfasta   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### createfontdatachunk.py

```bash
$ singularity exec <container> /usr/local/bin/createfontdatachunk.py
$ podman run --it --rm --entrypoint /usr/local/bin/createfontdatachunk.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/createfontdatachunk.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### htseq-count

```bash
$ singularity exec <container> /usr/local/bin/htseq-count
$ podman run --it --rm --entrypoint /usr/local/bin/htseq-count   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/htseq-count   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### htseq-qa

```bash
$ singularity exec <container> /usr/local/bin/htseq-qa
$ podman run --it --rm --entrypoint /usr/local/bin/htseq-qa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/htseq-qa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### enhancer.py

```bash
$ singularity exec <container> /usr/local/bin/enhancer.py
$ podman run --it --rm --entrypoint /usr/local/bin/enhancer.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/enhancer.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### explode.py

```bash
$ singularity exec <container> /usr/local/bin/explode.py
$ podman run --it --rm --entrypoint /usr/local/bin/explode.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/explode.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gifmaker.py

```bash
$ singularity exec <container> /usr/local/bin/gifmaker.py
$ podman run --it --rm --entrypoint /usr/local/bin/gifmaker.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gifmaker.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### painter.py

```bash
$ singularity exec <container> /usr/local/bin/painter.py
$ podman run --it --rm --entrypoint /usr/local/bin/painter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/painter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### player.py

```bash
$ singularity exec <container> /usr/local/bin/player.py
$ podman run --it --rm --entrypoint /usr/local/bin/player.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/player.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### thresholder.py

```bash
$ singularity exec <container> /usr/local/bin/thresholder.py
$ podman run --it --rm --entrypoint /usr/local/bin/thresholder.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/thresholder.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### viewer.py

```bash
$ singularity exec <container> /usr/local/bin/viewer.py
$ podman run --it --rm --entrypoint /usr/local/bin/viewer.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/viewer.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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