---
layout: container
name:  "quay.io/biocontainers/orthomcl"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/orthomcl/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/orthomcl/container.yaml"
updated_at: "2024-04-17 03:11:43.592726"
latest: "2.0.9--hdfd78af_5"
container_url: "https://biocontainers.pro/tools/orthomcl"
aliases:
 - "orthomclAdjustFasta"
 - "orthomclBlastParser"
 - "orthomclDropSchema"
 - "orthomclDumpPairsFiles"
 - "orthomclExtractProteinIdsFromGroupsFile"
 - "orthomclExtractProteinPairsFromGroupsFile"
 - "orthomclFilterFasta"
 - "orthomclInstallSchema"
 - "orthomclInstallSchema.sql"
 - "orthomclLoadBlast"
 - "orthomclLoadBlast.sql"
 - "orthomclMclToGroups"
 - "orthomclPairs"
 - "orthomclReduceFasta"
 - "orthomclReduceGroups"
 - "orthomclRemoveIdenticalGroups"
 - "orthomclSingletons"
 - "orthomclSortGroupMembersByScore"
 - "orthomclSortGroupsFile"
 - "clm"
 - "clmformat"
 - "clxdo"
 - "mcl"
 - "mclblastline"
 - "mclcm"
 - "mclpipeline"
 - "mcx"
 - "mcxarray"
 - "mcxassemble"
versions:
 - "2.0.9--hdfd78af_5"
description: "shpc-registry automated BioContainers addition for orthomcl"
config: {"url": "https://biocontainers.pro/tools/orthomcl", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for orthomcl", "latest": {"2.0.9--hdfd78af_5": "sha256:b27b8ffcc4652fd885fd532afc4317bd18abb371814aa437bd61fbd6ca1e93c4"}, "tags": {"2.0.9--hdfd78af_5": "sha256:b27b8ffcc4652fd885fd532afc4317bd18abb371814aa437bd61fbd6ca1e93c4"}, "docker": "quay.io/biocontainers/orthomcl", "aliases": {"orthomclAdjustFasta": "/usr/local/bin/orthomclAdjustFasta", "orthomclBlastParser": "/usr/local/bin/orthomclBlastParser", "orthomclDropSchema": "/usr/local/bin/orthomclDropSchema", "orthomclDumpPairsFiles": "/usr/local/bin/orthomclDumpPairsFiles", "orthomclExtractProteinIdsFromGroupsFile": "/usr/local/bin/orthomclExtractProteinIdsFromGroupsFile", "orthomclExtractProteinPairsFromGroupsFile": "/usr/local/bin/orthomclExtractProteinPairsFromGroupsFile", "orthomclFilterFasta": "/usr/local/bin/orthomclFilterFasta", "orthomclInstallSchema": "/usr/local/bin/orthomclInstallSchema", "orthomclInstallSchema.sql": "/usr/local/bin/orthomclInstallSchema.sql", "orthomclLoadBlast": "/usr/local/bin/orthomclLoadBlast", "orthomclLoadBlast.sql": "/usr/local/bin/orthomclLoadBlast.sql", "orthomclMclToGroups": "/usr/local/bin/orthomclMclToGroups", "orthomclPairs": "/usr/local/bin/orthomclPairs", "orthomclReduceFasta": "/usr/local/bin/orthomclReduceFasta", "orthomclReduceGroups": "/usr/local/bin/orthomclReduceGroups", "orthomclRemoveIdenticalGroups": "/usr/local/bin/orthomclRemoveIdenticalGroups", "orthomclSingletons": "/usr/local/bin/orthomclSingletons", "orthomclSortGroupMembersByScore": "/usr/local/bin/orthomclSortGroupMembersByScore", "orthomclSortGroupsFile": "/usr/local/bin/orthomclSortGroupsFile", "clm": "/usr/local/bin/clm", "clmformat": "/usr/local/bin/clmformat", "clxdo": "/usr/local/bin/clxdo", "mcl": "/usr/local/bin/mcl", "mclblastline": "/usr/local/bin/mclblastline", "mclcm": "/usr/local/bin/mclcm", "mclpipeline": "/usr/local/bin/mclpipeline", "mcx": "/usr/local/bin/mcx", "mcxarray": "/usr/local/bin/mcxarray", "mcxassemble": "/usr/local/bin/mcxassemble"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/orthomcl.
shpc-registry automated BioContainers addition for orthomcl
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/orthomcl
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/orthomcl:2.0.9--hdfd78af_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/orthomcl/2.0.9--hdfd78af_5
$ module help quay.io/biocontainers/orthomcl/2.0.9--hdfd78af_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### orthomcl-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### orthomcl-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### orthomcl-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### orthomcl-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### orthomcl-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### orthomcl-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### orthomclAdjustFasta

```bash
$ singularity exec <container> /usr/local/bin/orthomclAdjustFasta
$ podman run --it --rm --entrypoint /usr/local/bin/orthomclAdjustFasta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orthomclAdjustFasta   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### orthomclBlastParser

```bash
$ singularity exec <container> /usr/local/bin/orthomclBlastParser
$ podman run --it --rm --entrypoint /usr/local/bin/orthomclBlastParser   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orthomclBlastParser   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### orthomclDropSchema

```bash
$ singularity exec <container> /usr/local/bin/orthomclDropSchema
$ podman run --it --rm --entrypoint /usr/local/bin/orthomclDropSchema   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orthomclDropSchema   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### orthomclDumpPairsFiles

```bash
$ singularity exec <container> /usr/local/bin/orthomclDumpPairsFiles
$ podman run --it --rm --entrypoint /usr/local/bin/orthomclDumpPairsFiles   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orthomclDumpPairsFiles   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### orthomclExtractProteinIdsFromGroupsFile

```bash
$ singularity exec <container> /usr/local/bin/orthomclExtractProteinIdsFromGroupsFile
$ podman run --it --rm --entrypoint /usr/local/bin/orthomclExtractProteinIdsFromGroupsFile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orthomclExtractProteinIdsFromGroupsFile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### orthomclExtractProteinPairsFromGroupsFile

```bash
$ singularity exec <container> /usr/local/bin/orthomclExtractProteinPairsFromGroupsFile
$ podman run --it --rm --entrypoint /usr/local/bin/orthomclExtractProteinPairsFromGroupsFile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orthomclExtractProteinPairsFromGroupsFile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### orthomclFilterFasta

```bash
$ singularity exec <container> /usr/local/bin/orthomclFilterFasta
$ podman run --it --rm --entrypoint /usr/local/bin/orthomclFilterFasta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orthomclFilterFasta   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### orthomclInstallSchema

```bash
$ singularity exec <container> /usr/local/bin/orthomclInstallSchema
$ podman run --it --rm --entrypoint /usr/local/bin/orthomclInstallSchema   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orthomclInstallSchema   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### orthomclInstallSchema.sql

```bash
$ singularity exec <container> /usr/local/bin/orthomclInstallSchema.sql
$ podman run --it --rm --entrypoint /usr/local/bin/orthomclInstallSchema.sql   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orthomclInstallSchema.sql   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### orthomclLoadBlast

```bash
$ singularity exec <container> /usr/local/bin/orthomclLoadBlast
$ podman run --it --rm --entrypoint /usr/local/bin/orthomclLoadBlast   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orthomclLoadBlast   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### orthomclLoadBlast.sql

```bash
$ singularity exec <container> /usr/local/bin/orthomclLoadBlast.sql
$ podman run --it --rm --entrypoint /usr/local/bin/orthomclLoadBlast.sql   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orthomclLoadBlast.sql   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### orthomclMclToGroups

```bash
$ singularity exec <container> /usr/local/bin/orthomclMclToGroups
$ podman run --it --rm --entrypoint /usr/local/bin/orthomclMclToGroups   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orthomclMclToGroups   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### orthomclPairs

```bash
$ singularity exec <container> /usr/local/bin/orthomclPairs
$ podman run --it --rm --entrypoint /usr/local/bin/orthomclPairs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orthomclPairs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### orthomclReduceFasta

```bash
$ singularity exec <container> /usr/local/bin/orthomclReduceFasta
$ podman run --it --rm --entrypoint /usr/local/bin/orthomclReduceFasta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orthomclReduceFasta   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### orthomclReduceGroups

```bash
$ singularity exec <container> /usr/local/bin/orthomclReduceGroups
$ podman run --it --rm --entrypoint /usr/local/bin/orthomclReduceGroups   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orthomclReduceGroups   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### orthomclRemoveIdenticalGroups

```bash
$ singularity exec <container> /usr/local/bin/orthomclRemoveIdenticalGroups
$ podman run --it --rm --entrypoint /usr/local/bin/orthomclRemoveIdenticalGroups   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orthomclRemoveIdenticalGroups   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### orthomclSingletons

```bash
$ singularity exec <container> /usr/local/bin/orthomclSingletons
$ podman run --it --rm --entrypoint /usr/local/bin/orthomclSingletons   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orthomclSingletons   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### orthomclSortGroupMembersByScore

```bash
$ singularity exec <container> /usr/local/bin/orthomclSortGroupMembersByScore
$ podman run --it --rm --entrypoint /usr/local/bin/orthomclSortGroupMembersByScore   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orthomclSortGroupMembersByScore   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### orthomclSortGroupsFile

```bash
$ singularity exec <container> /usr/local/bin/orthomclSortGroupsFile
$ podman run --it --rm --entrypoint /usr/local/bin/orthomclSortGroupsFile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orthomclSortGroupsFile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clm

```bash
$ singularity exec <container> /usr/local/bin/clm
$ podman run --it --rm --entrypoint /usr/local/bin/clm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clmformat

```bash
$ singularity exec <container> /usr/local/bin/clmformat
$ podman run --it --rm --entrypoint /usr/local/bin/clmformat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clmformat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clxdo

```bash
$ singularity exec <container> /usr/local/bin/clxdo
$ podman run --it --rm --entrypoint /usr/local/bin/clxdo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clxdo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mcl

```bash
$ singularity exec <container> /usr/local/bin/mcl
$ podman run --it --rm --entrypoint /usr/local/bin/mcl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mcl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mclblastline

```bash
$ singularity exec <container> /usr/local/bin/mclblastline
$ podman run --it --rm --entrypoint /usr/local/bin/mclblastline   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mclblastline   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mclcm

```bash
$ singularity exec <container> /usr/local/bin/mclcm
$ podman run --it --rm --entrypoint /usr/local/bin/mclcm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mclcm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mclpipeline

```bash
$ singularity exec <container> /usr/local/bin/mclpipeline
$ podman run --it --rm --entrypoint /usr/local/bin/mclpipeline   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mclpipeline   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mcx

```bash
$ singularity exec <container> /usr/local/bin/mcx
$ podman run --it --rm --entrypoint /usr/local/bin/mcx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mcx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mcxarray

```bash
$ singularity exec <container> /usr/local/bin/mcxarray
$ podman run --it --rm --entrypoint /usr/local/bin/mcxarray   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mcxarray   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mcxassemble

```bash
$ singularity exec <container> /usr/local/bin/mcxassemble
$ podman run --it --rm --entrypoint /usr/local/bin/mcxassemble   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mcxassemble   -v ${PWD} -w ${PWD} <container> -c " $@"
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