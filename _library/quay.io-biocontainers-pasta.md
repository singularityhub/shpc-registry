---
layout: container
name:  "quay.io/biocontainers/pasta"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pasta/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pasta/container.yaml"
updated_at: "2024-12-29 03:20:56.642235"
latest: "1.9.2--py311hfad2c56_2"
container_url: "https://biocontainers.pro/tools/pasta"
aliases:
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
 - "prank"
 - "muscle"
 - "fasttree"
 - "sumlabels.py"
 - "sumtrees.py"
 - "clustalw2"
 - "mafft"
 - "hmmalign"
 - "hmmbuild"
 - "jaotc"
versions:
 - "1.7.8--py36h8c4c3a4_4"
 - "1.9.0--py39hf48a03f_0"
 - "1.9.0--py38h6805031_0"
 - "1.7.8--py37h8f50634_4"
 - "1.9.2--py38h703aefd_1"
 - "1.9.2--py311hfad2c56_2"
description: "shpc-registry automated BioContainers addition for pasta"
config: {"url": "https://biocontainers.pro/tools/pasta", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pasta", "latest": {"1.9.2--py311hfad2c56_2": "sha256:ef5c6031bd7f3e4dd6a793679d83d6a8af3a4d122dc6cd9991310ed7f8146e3c"}, "tags": {"1.7.8--py36h8c4c3a4_4": "sha256:3aa9f94be4732e32add993c19017df3ab6ed4a0465944450dfb219373f9f5d36", "1.9.0--py39hf48a03f_0": "sha256:f8d807d23493337085fbe54c8ad22c573c8820706033a2475cc6f18ad846731c", "1.9.0--py38h6805031_0": "sha256:567d94bcde91ace5e4fae48381223ada0da188f7446a4f947a5cac750306f60a", "1.7.8--py37h8f50634_4": "sha256:ea216e74289a54e38db618d564859e50e675c5978ddf1c401e38fdaa16e1891a", "1.9.2--py38h703aefd_1": "sha256:fd1a4d0aa29ac0f4160ff76023eec8bffad3bc40ce22523826ea612b8ee39788", "1.9.2--py311hfad2c56_2": "sha256:ef5c6031bd7f3e4dd6a793679d83d6a8af3a4d122dc6cd9991310ed7f8146e3c"}, "docker": "quay.io/biocontainers/pasta", "aliases": {"fakealigner": "/usr/local/bin/fakealigner", "faketree": "/usr/local/bin/faketree", "fasttreeMP": "/usr/local/bin/fasttreeMP", "hmmeralign": "/usr/local/bin/hmmeralign", "hmmerbuild": "/usr/local/bin/hmmerbuild", "opal.jar": "/usr/local/bin/opal.jar", "padaligner": "/usr/local/bin/padaligner", "randtree": "/usr/local/bin/randtree", "raxml": "/usr/local/bin/raxml", "raxmlp": "/usr/local/bin/raxmlp", "run_pasta.py": "/usr/local/bin/run_pasta.py", "run_pasta_gui.py": "/usr/local/bin/run_pasta_gui.py", "run_seqtools.py": "/usr/local/bin/run_seqtools.py", "prank": "/usr/local/bin/prank", "muscle": "/usr/local/bin/muscle", "fasttree": "/usr/local/bin/fasttree", "sumlabels.py": "/usr/local/bin/sumlabels.py", "sumtrees.py": "/usr/local/bin/sumtrees.py", "clustalw2": "/usr/local/bin/clustalw2", "mafft": "/usr/local/bin/mafft", "hmmalign": "/usr/local/bin/hmmalign", "hmmbuild": "/usr/local/bin/hmmbuild", "jaotc": "/usr/local/bin/jaotc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pasta.
shpc-registry automated BioContainers addition for pasta
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pasta
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pasta:1.9.2--py311hfad2c56_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pasta/1.9.2--py311hfad2c56_2
$ module help quay.io/biocontainers/pasta/1.9.2--py311hfad2c56_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pasta-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pasta-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pasta-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pasta-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pasta-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pasta-inspect-deffile:

```bash
$ singularity inspect -d <container>
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


#### prank

```bash
$ singularity exec <container> /usr/local/bin/prank
$ podman run --it --rm --entrypoint /usr/local/bin/prank   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prank   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### mafft

```bash
$ singularity exec <container> /usr/local/bin/mafft
$ podman run --it --rm --entrypoint /usr/local/bin/mafft   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mafft   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmalign

```bash
$ singularity exec <container> /usr/local/bin/hmmalign
$ podman run --it --rm --entrypoint /usr/local/bin/hmmalign   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmalign   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmbuild

```bash
$ singularity exec <container> /usr/local/bin/hmmbuild
$ podman run --it --rm --entrypoint /usr/local/bin/hmmbuild   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmbuild   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jaotc

```bash
$ singularity exec <container> /usr/local/bin/jaotc
$ podman run --it --rm --entrypoint /usr/local/bin/jaotc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jaotc   -v ${PWD} -w ${PWD} <container> -c " $@"
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