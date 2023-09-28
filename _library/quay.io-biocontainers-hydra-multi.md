---
layout: container
name:  "quay.io/biocontainers/hydra-multi"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/hydra-multi/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/hydra-multi/container.yaml"
updated_at: "2023-09-28 03:03:33.470297"
latest: "0.5.4--py27h43eeafb_3"
container_url: "https://biocontainers.pro/tools/hydra-multi"
aliases:
 - "assemble-routed-files.sh"
 - "bedpeToBam.py"
 - "bedpeToBed12.py"
 - "combine-assembled-files.sh"
 - "dedupDiscordantsMultiPass.py"
 - "extract_all_discordants.sh"
 - "extract_discordants.py"
 - "finalizeBreakpoints.py"
 - "forceOneClusterPerPairMem.py"
 - "frequency.py"
 - "hydra-assembler"
 - "hydra-ext"
 - "hydra-multi.sh"
 - "hydra-router"
 - "hydraToBreakpoint.py"
 - "make_hydra_config.py"
 - "mergeBreakpoints.py"
 - "pairDiscordants.py"
 - "bcftools"
 - "vcfutils.pl"
 - "shiftBed"
 - "annotateBed"
 - "bamToBed"
 - "bamToFastq"
 - "bed12ToBed6"
 - "bedToBam"
 - "bedToIgv"
 - "bedpeToBam"
versions:
 - "0.5.4--py27h5b5514e_2"
 - "0.5.4--py27h43eeafb_3"
description: "shpc-registry automated BioContainers addition for hydra-multi"
config: {"url": "https://biocontainers.pro/tools/hydra-multi", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for hydra-multi", "latest": {"0.5.4--py27h43eeafb_3": "sha256:350cbc9df652452f41a8220bbf67e0454709e58d9fe677af9e96fc0cb59e6f00"}, "tags": {"0.5.4--py27h5b5514e_2": "sha256:766594888b18519ace58e4fc245d9cab7c7af951dc7a6b0589c5b12ff4385e26", "0.5.4--py27h43eeafb_3": "sha256:350cbc9df652452f41a8220bbf67e0454709e58d9fe677af9e96fc0cb59e6f00"}, "docker": "quay.io/biocontainers/hydra-multi", "aliases": {"assemble-routed-files.sh": "/usr/local/bin/assemble-routed-files.sh", "bedpeToBam.py": "/usr/local/bin/bedpeToBam.py", "bedpeToBed12.py": "/usr/local/bin/bedpeToBed12.py", "combine-assembled-files.sh": "/usr/local/bin/combine-assembled-files.sh", "dedupDiscordantsMultiPass.py": "/usr/local/bin/dedupDiscordantsMultiPass.py", "extract_all_discordants.sh": "/usr/local/bin/extract_all_discordants.sh", "extract_discordants.py": "/usr/local/bin/extract_discordants.py", "finalizeBreakpoints.py": "/usr/local/bin/finalizeBreakpoints.py", "forceOneClusterPerPairMem.py": "/usr/local/bin/forceOneClusterPerPairMem.py", "frequency.py": "/usr/local/bin/frequency.py", "hydra-assembler": "/usr/local/bin/hydra-assembler", "hydra-ext": "/usr/local/bin/hydra-ext", "hydra-multi.sh": "/usr/local/bin/hydra-multi.sh", "hydra-router": "/usr/local/bin/hydra-router", "hydraToBreakpoint.py": "/usr/local/bin/hydraToBreakpoint.py", "make_hydra_config.py": "/usr/local/bin/make_hydra_config.py", "mergeBreakpoints.py": "/usr/local/bin/mergeBreakpoints.py", "pairDiscordants.py": "/usr/local/bin/pairDiscordants.py", "bcftools": "/usr/local/bin/bcftools", "vcfutils.pl": "/usr/local/bin/vcfutils.pl", "shiftBed": "/usr/local/bin/shiftBed", "annotateBed": "/usr/local/bin/annotateBed", "bamToBed": "/usr/local/bin/bamToBed", "bamToFastq": "/usr/local/bin/bamToFastq", "bed12ToBed6": "/usr/local/bin/bed12ToBed6", "bedToBam": "/usr/local/bin/bedToBam", "bedToIgv": "/usr/local/bin/bedToIgv", "bedpeToBam": "/usr/local/bin/bedpeToBam"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/hydra-multi.
shpc-registry automated BioContainers addition for hydra-multi
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/hydra-multi
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/hydra-multi:0.5.4--py27h43eeafb_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/hydra-multi/0.5.4--py27h43eeafb_3
$ module help quay.io/biocontainers/hydra-multi/0.5.4--py27h43eeafb_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### hydra-multi-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### hydra-multi-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### hydra-multi-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### hydra-multi-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### hydra-multi-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### hydra-multi-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### assemble-routed-files.sh

```bash
$ singularity exec <container> /usr/local/bin/assemble-routed-files.sh
$ podman run --it --rm --entrypoint /usr/local/bin/assemble-routed-files.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/assemble-routed-files.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bedpeToBam.py

```bash
$ singularity exec <container> /usr/local/bin/bedpeToBam.py
$ podman run --it --rm --entrypoint /usr/local/bin/bedpeToBam.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedpeToBam.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bedpeToBed12.py

```bash
$ singularity exec <container> /usr/local/bin/bedpeToBed12.py
$ podman run --it --rm --entrypoint /usr/local/bin/bedpeToBed12.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedpeToBed12.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### combine-assembled-files.sh

```bash
$ singularity exec <container> /usr/local/bin/combine-assembled-files.sh
$ podman run --it --rm --entrypoint /usr/local/bin/combine-assembled-files.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/combine-assembled-files.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dedupDiscordantsMultiPass.py

```bash
$ singularity exec <container> /usr/local/bin/dedupDiscordantsMultiPass.py
$ podman run --it --rm --entrypoint /usr/local/bin/dedupDiscordantsMultiPass.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dedupDiscordantsMultiPass.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extract_all_discordants.sh

```bash
$ singularity exec <container> /usr/local/bin/extract_all_discordants.sh
$ podman run --it --rm --entrypoint /usr/local/bin/extract_all_discordants.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extract_all_discordants.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extract_discordants.py

```bash
$ singularity exec <container> /usr/local/bin/extract_discordants.py
$ podman run --it --rm --entrypoint /usr/local/bin/extract_discordants.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extract_discordants.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### finalizeBreakpoints.py

```bash
$ singularity exec <container> /usr/local/bin/finalizeBreakpoints.py
$ podman run --it --rm --entrypoint /usr/local/bin/finalizeBreakpoints.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/finalizeBreakpoints.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### forceOneClusterPerPairMem.py

```bash
$ singularity exec <container> /usr/local/bin/forceOneClusterPerPairMem.py
$ podman run --it --rm --entrypoint /usr/local/bin/forceOneClusterPerPairMem.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/forceOneClusterPerPairMem.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### frequency.py

```bash
$ singularity exec <container> /usr/local/bin/frequency.py
$ podman run --it --rm --entrypoint /usr/local/bin/frequency.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/frequency.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hydra-assembler

```bash
$ singularity exec <container> /usr/local/bin/hydra-assembler
$ podman run --it --rm --entrypoint /usr/local/bin/hydra-assembler   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hydra-assembler   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hydra-ext

```bash
$ singularity exec <container> /usr/local/bin/hydra-ext
$ podman run --it --rm --entrypoint /usr/local/bin/hydra-ext   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hydra-ext   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hydra-multi.sh

```bash
$ singularity exec <container> /usr/local/bin/hydra-multi.sh
$ podman run --it --rm --entrypoint /usr/local/bin/hydra-multi.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hydra-multi.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hydra-router

```bash
$ singularity exec <container> /usr/local/bin/hydra-router
$ podman run --it --rm --entrypoint /usr/local/bin/hydra-router   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hydra-router   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hydraToBreakpoint.py

```bash
$ singularity exec <container> /usr/local/bin/hydraToBreakpoint.py
$ podman run --it --rm --entrypoint /usr/local/bin/hydraToBreakpoint.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hydraToBreakpoint.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### make_hydra_config.py

```bash
$ singularity exec <container> /usr/local/bin/make_hydra_config.py
$ podman run --it --rm --entrypoint /usr/local/bin/make_hydra_config.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/make_hydra_config.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mergeBreakpoints.py

```bash
$ singularity exec <container> /usr/local/bin/mergeBreakpoints.py
$ podman run --it --rm --entrypoint /usr/local/bin/mergeBreakpoints.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mergeBreakpoints.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pairDiscordants.py

```bash
$ singularity exec <container> /usr/local/bin/pairDiscordants.py
$ podman run --it --rm --entrypoint /usr/local/bin/pairDiscordants.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pairDiscordants.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bcftools

```bash
$ singularity exec <container> /usr/local/bin/bcftools
$ podman run --it --rm --entrypoint /usr/local/bin/bcftools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bcftools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcfutils.pl

```bash
$ singularity exec <container> /usr/local/bin/vcfutils.pl
$ podman run --it --rm --entrypoint /usr/local/bin/vcfutils.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcfutils.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shiftBed

```bash
$ singularity exec <container> /usr/local/bin/shiftBed
$ podman run --it --rm --entrypoint /usr/local/bin/shiftBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shiftBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annotateBed

```bash
$ singularity exec <container> /usr/local/bin/annotateBed
$ podman run --it --rm --entrypoint /usr/local/bin/annotateBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annotateBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamToBed

```bash
$ singularity exec <container> /usr/local/bin/bamToBed
$ podman run --it --rm --entrypoint /usr/local/bin/bamToBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamToBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamToFastq

```bash
$ singularity exec <container> /usr/local/bin/bamToFastq
$ podman run --it --rm --entrypoint /usr/local/bin/bamToFastq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamToFastq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bed12ToBed6

```bash
$ singularity exec <container> /usr/local/bin/bed12ToBed6
$ podman run --it --rm --entrypoint /usr/local/bin/bed12ToBed6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bed12ToBed6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bedToBam

```bash
$ singularity exec <container> /usr/local/bin/bedToBam
$ podman run --it --rm --entrypoint /usr/local/bin/bedToBam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedToBam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bedToIgv

```bash
$ singularity exec <container> /usr/local/bin/bedToIgv
$ podman run --it --rm --entrypoint /usr/local/bin/bedToIgv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedToIgv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bedpeToBam

```bash
$ singularity exec <container> /usr/local/bin/bedpeToBam
$ podman run --it --rm --entrypoint /usr/local/bin/bedpeToBam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedpeToBam   -v ${PWD} -w ${PWD} <container> -c " $@"
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