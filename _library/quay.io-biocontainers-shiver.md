---
layout: container
name:  "quay.io/biocontainers/shiver"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/shiver/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/shiver/container.yaml"
updated_at: "2025-11-14 03:28:53.781511"
latest: "1.7.3--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/shiver"
aliases:
 - "basqcol"
 - "fetchseq"
 - "mixreads"
 - "readstats"
 - "shiver_align_contigs.sh"
 - "shiver_config.sh"
 - "shiver_full_auto.sh"
 - "shiver_funcs.sh"
 - "shiver_init.sh"
 - "shiver_map_reads.sh"
 - "shiver_reprocess_bam.sh"
 - "simqual"
 - "simread"
 - "smalt"
 - "splitmates"
 - "splitreads"
 - "trunkreads"
 - "createfontdatachunk.py"
 - "picard"
 - "enhancer.py"
 - "explode.py"
 - "fastaq"
 - "gifmaker.py"
 - "painter.py"
 - "player.py"
 - "thresholder.py"
 - "viewer.py"
versions:
 - "1.3.5--py35_0"
 - "1.3.5--py27_0"
 - "1.7.3--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for shiver"
config: {"url": "https://biocontainers.pro/tools/shiver", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for shiver", "latest": {"1.7.3--hdfd78af_0": "sha256:4360c6df02099b66a39321220d19efadf1073ca4b524a516717aa43049675733"}, "tags": {"1.3.5--py35_0": "sha256:18de85d5a08b19ca795467009dbffa3ab3d010a4f8e11d1ce05a0016edcc81ec", "1.3.5--py27_0": "sha256:8d54d1dcca0de616a0f4849bcad9a30a251df8a2f136b5b3ab2f91d1b5df0d02", "1.7.3--hdfd78af_0": "sha256:4360c6df02099b66a39321220d19efadf1073ca4b524a516717aa43049675733"}, "docker": "quay.io/biocontainers/shiver", "aliases": {"basqcol": "/usr/local/bin/basqcol", "fetchseq": "/usr/local/bin/fetchseq", "mixreads": "/usr/local/bin/mixreads", "readstats": "/usr/local/bin/readstats", "shiver_align_contigs.sh": "/usr/local/bin/shiver_align_contigs.sh", "shiver_config.sh": "/usr/local/bin/shiver_config.sh", "shiver_full_auto.sh": "/usr/local/bin/shiver_full_auto.sh", "shiver_funcs.sh": "/usr/local/bin/shiver_funcs.sh", "shiver_init.sh": "/usr/local/bin/shiver_init.sh", "shiver_map_reads.sh": "/usr/local/bin/shiver_map_reads.sh", "shiver_reprocess_bam.sh": "/usr/local/bin/shiver_reprocess_bam.sh", "simqual": "/usr/local/bin/simqual", "simread": "/usr/local/bin/simread", "smalt": "/usr/local/bin/smalt", "splitmates": "/usr/local/bin/splitmates", "splitreads": "/usr/local/bin/splitreads", "trunkreads": "/usr/local/bin/trunkreads", "createfontdatachunk.py": "/usr/local/bin/createfontdatachunk.py", "picard": "/usr/local/bin/picard", "enhancer.py": "/usr/local/bin/enhancer.py", "explode.py": "/usr/local/bin/explode.py", "fastaq": "/usr/local/bin/fastaq", "gifmaker.py": "/usr/local/bin/gifmaker.py", "painter.py": "/usr/local/bin/painter.py", "player.py": "/usr/local/bin/player.py", "thresholder.py": "/usr/local/bin/thresholder.py", "viewer.py": "/usr/local/bin/viewer.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/shiver.
shpc-registry automated BioContainers addition for shiver
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/shiver
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/shiver:1.7.3--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/shiver/1.7.3--hdfd78af_0
$ module help quay.io/biocontainers/shiver/1.7.3--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### shiver-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### shiver-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### shiver-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### shiver-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### shiver-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### shiver-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### basqcol

```bash
$ singularity exec <container> /usr/local/bin/basqcol
$ podman run --it --rm --entrypoint /usr/local/bin/basqcol   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/basqcol   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fetchseq

```bash
$ singularity exec <container> /usr/local/bin/fetchseq
$ podman run --it --rm --entrypoint /usr/local/bin/fetchseq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fetchseq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mixreads

```bash
$ singularity exec <container> /usr/local/bin/mixreads
$ podman run --it --rm --entrypoint /usr/local/bin/mixreads   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mixreads   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### readstats

```bash
$ singularity exec <container> /usr/local/bin/readstats
$ podman run --it --rm --entrypoint /usr/local/bin/readstats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/readstats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shiver_align_contigs.sh

```bash
$ singularity exec <container> /usr/local/bin/shiver_align_contigs.sh
$ podman run --it --rm --entrypoint /usr/local/bin/shiver_align_contigs.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shiver_align_contigs.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shiver_config.sh

```bash
$ singularity exec <container> /usr/local/bin/shiver_config.sh
$ podman run --it --rm --entrypoint /usr/local/bin/shiver_config.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shiver_config.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shiver_full_auto.sh

```bash
$ singularity exec <container> /usr/local/bin/shiver_full_auto.sh
$ podman run --it --rm --entrypoint /usr/local/bin/shiver_full_auto.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shiver_full_auto.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shiver_funcs.sh

```bash
$ singularity exec <container> /usr/local/bin/shiver_funcs.sh
$ podman run --it --rm --entrypoint /usr/local/bin/shiver_funcs.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shiver_funcs.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shiver_init.sh

```bash
$ singularity exec <container> /usr/local/bin/shiver_init.sh
$ podman run --it --rm --entrypoint /usr/local/bin/shiver_init.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shiver_init.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shiver_map_reads.sh

```bash
$ singularity exec <container> /usr/local/bin/shiver_map_reads.sh
$ podman run --it --rm --entrypoint /usr/local/bin/shiver_map_reads.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shiver_map_reads.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shiver_reprocess_bam.sh

```bash
$ singularity exec <container> /usr/local/bin/shiver_reprocess_bam.sh
$ podman run --it --rm --entrypoint /usr/local/bin/shiver_reprocess_bam.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shiver_reprocess_bam.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### simqual

```bash
$ singularity exec <container> /usr/local/bin/simqual
$ podman run --it --rm --entrypoint /usr/local/bin/simqual   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/simqual   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### simread

```bash
$ singularity exec <container> /usr/local/bin/simread
$ podman run --it --rm --entrypoint /usr/local/bin/simread   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/simread   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### smalt

```bash
$ singularity exec <container> /usr/local/bin/smalt
$ podman run --it --rm --entrypoint /usr/local/bin/smalt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/smalt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### splitmates

```bash
$ singularity exec <container> /usr/local/bin/splitmates
$ podman run --it --rm --entrypoint /usr/local/bin/splitmates   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/splitmates   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### splitreads

```bash
$ singularity exec <container> /usr/local/bin/splitreads
$ podman run --it --rm --entrypoint /usr/local/bin/splitreads   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/splitreads   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trunkreads

```bash
$ singularity exec <container> /usr/local/bin/trunkreads
$ podman run --it --rm --entrypoint /usr/local/bin/trunkreads   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trunkreads   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### createfontdatachunk.py

```bash
$ singularity exec <container> /usr/local/bin/createfontdatachunk.py
$ podman run --it --rm --entrypoint /usr/local/bin/createfontdatachunk.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/createfontdatachunk.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### picard

```bash
$ singularity exec <container> /usr/local/bin/picard
$ podman run --it --rm --entrypoint /usr/local/bin/picard   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/picard   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### fastaq

```bash
$ singularity exec <container> /usr/local/bin/fastaq
$ podman run --it --rm --entrypoint /usr/local/bin/fastaq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastaq   -v ${PWD} -w ${PWD} <container> -c " $@"
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