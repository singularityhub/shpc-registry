---
layout: container
name:  "quay.io/biocontainers/agora"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/agora/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/agora/container.yaml"
updated_at: "2026-06-06 15:56:53.573346"
latest: "3.1--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/agora"
aliases:
 - "ALL.extractGeneFamilies.py"
 - "ALL.filterBlocks-fixedLength.py"
 - "ALL.filterBlocks-propLength.py"
 - "ALL.filterGeneFamilies-size.py"
 - "ALL.reformatGeneFamilies.py"
 - "ALL.selectBestReconstruction.py"
 - "ENSEMBL.buildProteinTrees.py"
 - "agora-basic.py"
 - "agora-generic.py"
 - "agora-plants.py"
 - "agora-vertebrates.py"
 - "agora.py"
 - "buildSynteny.integr-copy.py"
 - "buildSynteny.integr-denovo.py"
 - "buildSynteny.integr-fillin.py"
 - "buildSynteny.integr-fusion.py"
 - "buildSynteny.integr-insertion.py"
 - "buildSynteny.integr-scaffolds.py"
 - "buildSynteny.pairwise-conservedAdjacencies.py"
 - "buildSynteny.pairwise-conservedPairs.py"
 - "convert.ancGenomes.blocks-of-blocks-to-blocks-of-ancGenes.py"
 - "convert.ancGenomes.blocks-to-genes.py"
 - "misc.compareGenomes.py"
 - "idle3.14"
 - "pydoc3.14"
 - "python3.14"
 - "python3.14-config"
versions:
 - "3.1--hdfd78af_0"
description: "singularity registry hpc automated addition for agora"
config: {"url": "https://biocontainers.pro/tools/agora", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for agora", "latest": {"3.1--hdfd78af_0": "sha256:275d20fe7d8a01bf4e70b48e44c62ed8dca335b13d6fc5179e068943ccf61d42"}, "tags": {"3.1--hdfd78af_0": "sha256:275d20fe7d8a01bf4e70b48e44c62ed8dca335b13d6fc5179e068943ccf61d42"}, "docker": "quay.io/biocontainers/agora", "aliases": {"ALL.extractGeneFamilies.py": "/usr/local/bin/ALL.extractGeneFamilies.py", "ALL.filterBlocks-fixedLength.py": "/usr/local/bin/ALL.filterBlocks-fixedLength.py", "ALL.filterBlocks-propLength.py": "/usr/local/bin/ALL.filterBlocks-propLength.py", "ALL.filterGeneFamilies-size.py": "/usr/local/bin/ALL.filterGeneFamilies-size.py", "ALL.reformatGeneFamilies.py": "/usr/local/bin/ALL.reformatGeneFamilies.py", "ALL.selectBestReconstruction.py": "/usr/local/bin/ALL.selectBestReconstruction.py", "ENSEMBL.buildProteinTrees.py": "/usr/local/bin/ENSEMBL.buildProteinTrees.py", "agora-basic.py": "/usr/local/bin/agora-basic.py", "agora-generic.py": "/usr/local/bin/agora-generic.py", "agora-plants.py": "/usr/local/bin/agora-plants.py", "agora-vertebrates.py": "/usr/local/bin/agora-vertebrates.py", "agora.py": "/usr/local/bin/agora.py", "buildSynteny.integr-copy.py": "/usr/local/bin/buildSynteny.integr-copy.py", "buildSynteny.integr-denovo.py": "/usr/local/bin/buildSynteny.integr-denovo.py", "buildSynteny.integr-fillin.py": "/usr/local/bin/buildSynteny.integr-fillin.py", "buildSynteny.integr-fusion.py": "/usr/local/bin/buildSynteny.integr-fusion.py", "buildSynteny.integr-insertion.py": "/usr/local/bin/buildSynteny.integr-insertion.py", "buildSynteny.integr-scaffolds.py": "/usr/local/bin/buildSynteny.integr-scaffolds.py", "buildSynteny.pairwise-conservedAdjacencies.py": "/usr/local/bin/buildSynteny.pairwise-conservedAdjacencies.py", "buildSynteny.pairwise-conservedPairs.py": "/usr/local/bin/buildSynteny.pairwise-conservedPairs.py", "convert.ancGenomes.blocks-of-blocks-to-blocks-of-ancGenes.py": "/usr/local/bin/convert.ancGenomes.blocks-of-blocks-to-blocks-of-ancGenes.py", "convert.ancGenomes.blocks-to-genes.py": "/usr/local/bin/convert.ancGenomes.blocks-to-genes.py", "misc.compareGenomes.py": "/usr/local/bin/misc.compareGenomes.py", "idle3.14": "/usr/local/bin/idle3.14", "pydoc3.14": "/usr/local/bin/pydoc3.14", "python3.14": "/usr/local/bin/python3.14", "python3.14-config": "/usr/local/bin/python3.14-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/agora.
singularity registry hpc automated addition for agora
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/agora
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/agora:3.1--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/agora/3.1--hdfd78af_0
$ module help quay.io/biocontainers/agora/3.1--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### agora-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### agora-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### agora-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### agora-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### agora-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### agora-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ALL.extractGeneFamilies.py

```bash
$ singularity exec <container> /usr/local/bin/ALL.extractGeneFamilies.py
$ podman run --it --rm --entrypoint /usr/local/bin/ALL.extractGeneFamilies.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ALL.extractGeneFamilies.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ALL.filterBlocks-fixedLength.py

```bash
$ singularity exec <container> /usr/local/bin/ALL.filterBlocks-fixedLength.py
$ podman run --it --rm --entrypoint /usr/local/bin/ALL.filterBlocks-fixedLength.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ALL.filterBlocks-fixedLength.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ALL.filterBlocks-propLength.py

```bash
$ singularity exec <container> /usr/local/bin/ALL.filterBlocks-propLength.py
$ podman run --it --rm --entrypoint /usr/local/bin/ALL.filterBlocks-propLength.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ALL.filterBlocks-propLength.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ALL.filterGeneFamilies-size.py

```bash
$ singularity exec <container> /usr/local/bin/ALL.filterGeneFamilies-size.py
$ podman run --it --rm --entrypoint /usr/local/bin/ALL.filterGeneFamilies-size.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ALL.filterGeneFamilies-size.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ALL.reformatGeneFamilies.py

```bash
$ singularity exec <container> /usr/local/bin/ALL.reformatGeneFamilies.py
$ podman run --it --rm --entrypoint /usr/local/bin/ALL.reformatGeneFamilies.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ALL.reformatGeneFamilies.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ALL.selectBestReconstruction.py

```bash
$ singularity exec <container> /usr/local/bin/ALL.selectBestReconstruction.py
$ podman run --it --rm --entrypoint /usr/local/bin/ALL.selectBestReconstruction.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ALL.selectBestReconstruction.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ENSEMBL.buildProteinTrees.py

```bash
$ singularity exec <container> /usr/local/bin/ENSEMBL.buildProteinTrees.py
$ podman run --it --rm --entrypoint /usr/local/bin/ENSEMBL.buildProteinTrees.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ENSEMBL.buildProteinTrees.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### agora-basic.py

```bash
$ singularity exec <container> /usr/local/bin/agora-basic.py
$ podman run --it --rm --entrypoint /usr/local/bin/agora-basic.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/agora-basic.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### agora-generic.py

```bash
$ singularity exec <container> /usr/local/bin/agora-generic.py
$ podman run --it --rm --entrypoint /usr/local/bin/agora-generic.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/agora-generic.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### agora-plants.py

```bash
$ singularity exec <container> /usr/local/bin/agora-plants.py
$ podman run --it --rm --entrypoint /usr/local/bin/agora-plants.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/agora-plants.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### agora-vertebrates.py

```bash
$ singularity exec <container> /usr/local/bin/agora-vertebrates.py
$ podman run --it --rm --entrypoint /usr/local/bin/agora-vertebrates.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/agora-vertebrates.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### agora.py

```bash
$ singularity exec <container> /usr/local/bin/agora.py
$ podman run --it --rm --entrypoint /usr/local/bin/agora.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/agora.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### buildSynteny.integr-copy.py

```bash
$ singularity exec <container> /usr/local/bin/buildSynteny.integr-copy.py
$ podman run --it --rm --entrypoint /usr/local/bin/buildSynteny.integr-copy.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/buildSynteny.integr-copy.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### buildSynteny.integr-denovo.py

```bash
$ singularity exec <container> /usr/local/bin/buildSynteny.integr-denovo.py
$ podman run --it --rm --entrypoint /usr/local/bin/buildSynteny.integr-denovo.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/buildSynteny.integr-denovo.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### buildSynteny.integr-fillin.py

```bash
$ singularity exec <container> /usr/local/bin/buildSynteny.integr-fillin.py
$ podman run --it --rm --entrypoint /usr/local/bin/buildSynteny.integr-fillin.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/buildSynteny.integr-fillin.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### buildSynteny.integr-fusion.py

```bash
$ singularity exec <container> /usr/local/bin/buildSynteny.integr-fusion.py
$ podman run --it --rm --entrypoint /usr/local/bin/buildSynteny.integr-fusion.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/buildSynteny.integr-fusion.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### buildSynteny.integr-insertion.py

```bash
$ singularity exec <container> /usr/local/bin/buildSynteny.integr-insertion.py
$ podman run --it --rm --entrypoint /usr/local/bin/buildSynteny.integr-insertion.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/buildSynteny.integr-insertion.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### buildSynteny.integr-scaffolds.py

```bash
$ singularity exec <container> /usr/local/bin/buildSynteny.integr-scaffolds.py
$ podman run --it --rm --entrypoint /usr/local/bin/buildSynteny.integr-scaffolds.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/buildSynteny.integr-scaffolds.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### buildSynteny.pairwise-conservedAdjacencies.py

```bash
$ singularity exec <container> /usr/local/bin/buildSynteny.pairwise-conservedAdjacencies.py
$ podman run --it --rm --entrypoint /usr/local/bin/buildSynteny.pairwise-conservedAdjacencies.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/buildSynteny.pairwise-conservedAdjacencies.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### buildSynteny.pairwise-conservedPairs.py

```bash
$ singularity exec <container> /usr/local/bin/buildSynteny.pairwise-conservedPairs.py
$ podman run --it --rm --entrypoint /usr/local/bin/buildSynteny.pairwise-conservedPairs.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/buildSynteny.pairwise-conservedPairs.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### convert.ancGenomes.blocks-of-blocks-to-blocks-of-ancGenes.py

```bash
$ singularity exec <container> /usr/local/bin/convert.ancGenomes.blocks-of-blocks-to-blocks-of-ancGenes.py
$ podman run --it --rm --entrypoint /usr/local/bin/convert.ancGenomes.blocks-of-blocks-to-blocks-of-ancGenes.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convert.ancGenomes.blocks-of-blocks-to-blocks-of-ancGenes.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### convert.ancGenomes.blocks-to-genes.py

```bash
$ singularity exec <container> /usr/local/bin/convert.ancGenomes.blocks-to-genes.py
$ podman run --it --rm --entrypoint /usr/local/bin/convert.ancGenomes.blocks-to-genes.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convert.ancGenomes.blocks-to-genes.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### misc.compareGenomes.py

```bash
$ singularity exec <container> /usr/local/bin/misc.compareGenomes.py
$ podman run --it --rm --entrypoint /usr/local/bin/misc.compareGenomes.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/misc.compareGenomes.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.14

```bash
$ singularity exec <container> /usr/local/bin/idle3.14
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.14

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.14
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.14

```bash
$ singularity exec <container> /usr/local/bin/python3.14
$ podman run --it --rm --entrypoint /usr/local/bin/python3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.14-config

```bash
$ singularity exec <container> /usr/local/bin/python3.14-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.14-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.14-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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