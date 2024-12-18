---
layout: container
name:  "quay.io/biocontainers/plant_tribes_gene_family_aligner"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/plant_tribes_gene_family_aligner/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/plant_tribes_gene_family_aligner/container.yaml"
updated_at: "2024-12-18 03:46:23.757074"
latest: "1.0.4--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/plant_tribes_gene_family_aligner"
aliases:
 - "GeneFamilyAligner"
 - "fakealigner"
 - "faketree"
 - "fasttreeMP"
 - "hmmeralign"
 - "hmmerbuild"
 - "opal.jar"
 - "padaligner"
 - "randtree"
 - "raxml"
 - "raxmlp"
 - "run_pasta.py"
 - "run_pasta_gui.py"
 - "run_seqtools.py"
 - "readal"
 - "statal"
 - "trimal"
 - "prank"
 - "dendropy-format"
 - "muscle"
 - "fasttree"
 - "sumlabels.py"
 - "sumtrees.py"
 - "clustalw2"
versions:
 - "1.0.4--hdfd78af_1"
description: "shpc-registry automated BioContainers addition for plant_tribes_gene_family_aligner"
config: {"url": "https://biocontainers.pro/tools/plant_tribes_gene_family_aligner", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for plant_tribes_gene_family_aligner", "latest": {"1.0.4--hdfd78af_1": "sha256:b58eec981f9a05caff325842baadeb0aa164ec53ab0c7facecde085fb45b4313"}, "tags": {"1.0.4--hdfd78af_1": "sha256:b58eec981f9a05caff325842baadeb0aa164ec53ab0c7facecde085fb45b4313"}, "docker": "quay.io/biocontainers/plant_tribes_gene_family_aligner", "aliases": {"GeneFamilyAligner": "/usr/local/bin/GeneFamilyAligner", "fakealigner": "/usr/local/bin/fakealigner", "faketree": "/usr/local/bin/faketree", "fasttreeMP": "/usr/local/bin/fasttreeMP", "hmmeralign": "/usr/local/bin/hmmeralign", "hmmerbuild": "/usr/local/bin/hmmerbuild", "opal.jar": "/usr/local/bin/opal.jar", "padaligner": "/usr/local/bin/padaligner", "randtree": "/usr/local/bin/randtree", "raxml": "/usr/local/bin/raxml", "raxmlp": "/usr/local/bin/raxmlp", "run_pasta.py": "/usr/local/bin/run_pasta.py", "run_pasta_gui.py": "/usr/local/bin/run_pasta_gui.py", "run_seqtools.py": "/usr/local/bin/run_seqtools.py", "readal": "/usr/local/bin/readal", "statal": "/usr/local/bin/statal", "trimal": "/usr/local/bin/trimal", "prank": "/usr/local/bin/prank", "dendropy-format": "/usr/local/bin/dendropy-format", "muscle": "/usr/local/bin/muscle", "fasttree": "/usr/local/bin/fasttree", "sumlabels.py": "/usr/local/bin/sumlabels.py", "sumtrees.py": "/usr/local/bin/sumtrees.py", "clustalw2": "/usr/local/bin/clustalw2"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/plant_tribes_gene_family_aligner.
shpc-registry automated BioContainers addition for plant_tribes_gene_family_aligner
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/plant_tribes_gene_family_aligner
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/plant_tribes_gene_family_aligner:1.0.4--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/plant_tribes_gene_family_aligner/1.0.4--hdfd78af_1
$ module help quay.io/biocontainers/plant_tribes_gene_family_aligner/1.0.4--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### plant_tribes_gene_family_aligner-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### plant_tribes_gene_family_aligner-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### plant_tribes_gene_family_aligner-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### plant_tribes_gene_family_aligner-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### plant_tribes_gene_family_aligner-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### plant_tribes_gene_family_aligner-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### GeneFamilyAligner

```bash
$ singularity exec <container> /usr/local/bin/GeneFamilyAligner
$ podman run --it --rm --entrypoint /usr/local/bin/GeneFamilyAligner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GeneFamilyAligner   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fakealigner

```bash
$ singularity exec <container> /usr/local/bin/fakealigner
$ podman run --it --rm --entrypoint /usr/local/bin/fakealigner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fakealigner   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### faketree

```bash
$ singularity exec <container> /usr/local/bin/faketree
$ podman run --it --rm --entrypoint /usr/local/bin/faketree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/faketree   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasttreeMP

```bash
$ singularity exec <container> /usr/local/bin/fasttreeMP
$ podman run --it --rm --entrypoint /usr/local/bin/fasttreeMP   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasttreeMP   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmeralign

```bash
$ singularity exec <container> /usr/local/bin/hmmeralign
$ podman run --it --rm --entrypoint /usr/local/bin/hmmeralign   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmeralign   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmerbuild

```bash
$ singularity exec <container> /usr/local/bin/hmmerbuild
$ podman run --it --rm --entrypoint /usr/local/bin/hmmerbuild   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmerbuild   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### opal.jar

```bash
$ singularity exec <container> /usr/local/bin/opal.jar
$ podman run --it --rm --entrypoint /usr/local/bin/opal.jar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/opal.jar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### padaligner

```bash
$ singularity exec <container> /usr/local/bin/padaligner
$ podman run --it --rm --entrypoint /usr/local/bin/padaligner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/padaligner   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### randtree

```bash
$ singularity exec <container> /usr/local/bin/randtree
$ podman run --it --rm --entrypoint /usr/local/bin/randtree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/randtree   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### raxml

```bash
$ singularity exec <container> /usr/local/bin/raxml
$ podman run --it --rm --entrypoint /usr/local/bin/raxml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/raxml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### raxmlp

```bash
$ singularity exec <container> /usr/local/bin/raxmlp
$ podman run --it --rm --entrypoint /usr/local/bin/raxmlp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/raxmlp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_pasta.py

```bash
$ singularity exec <container> /usr/local/bin/run_pasta.py
$ podman run --it --rm --entrypoint /usr/local/bin/run_pasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_pasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_pasta_gui.py

```bash
$ singularity exec <container> /usr/local/bin/run_pasta_gui.py
$ podman run --it --rm --entrypoint /usr/local/bin/run_pasta_gui.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_pasta_gui.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_seqtools.py

```bash
$ singularity exec <container> /usr/local/bin/run_seqtools.py
$ podman run --it --rm --entrypoint /usr/local/bin/run_seqtools.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_seqtools.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### readal

```bash
$ singularity exec <container> /usr/local/bin/readal
$ podman run --it --rm --entrypoint /usr/local/bin/readal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/readal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### statal

```bash
$ singularity exec <container> /usr/local/bin/statal
$ podman run --it --rm --entrypoint /usr/local/bin/statal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/statal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trimal

```bash
$ singularity exec <container> /usr/local/bin/trimal
$ podman run --it --rm --entrypoint /usr/local/bin/trimal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trimal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prank

```bash
$ singularity exec <container> /usr/local/bin/prank
$ podman run --it --rm --entrypoint /usr/local/bin/prank   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prank   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dendropy-format

```bash
$ singularity exec <container> /usr/local/bin/dendropy-format
$ podman run --it --rm --entrypoint /usr/local/bin/dendropy-format   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dendropy-format   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### muscle

```bash
$ singularity exec <container> /usr/local/bin/muscle
$ podman run --it --rm --entrypoint /usr/local/bin/muscle   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/muscle   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasttree

```bash
$ singularity exec <container> /usr/local/bin/fasttree
$ podman run --it --rm --entrypoint /usr/local/bin/fasttree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasttree   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sumlabels.py

```bash
$ singularity exec <container> /usr/local/bin/sumlabels.py
$ podman run --it --rm --entrypoint /usr/local/bin/sumlabels.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sumlabels.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sumtrees.py

```bash
$ singularity exec <container> /usr/local/bin/sumtrees.py
$ podman run --it --rm --entrypoint /usr/local/bin/sumtrees.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sumtrees.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clustalw2

```bash
$ singularity exec <container> /usr/local/bin/clustalw2
$ podman run --it --rm --entrypoint /usr/local/bin/clustalw2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clustalw2   -v ${PWD} -w ${PWD} <container> -c " $@"
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