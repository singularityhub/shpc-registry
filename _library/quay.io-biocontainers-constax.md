---
layout: container
name:  "quay.io/biocontainers/constax"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/constax/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/constax/container.yaml"
updated_at: "2023-10-24 03:05:28.108908"
latest: "2.0.20--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/constax"
aliases:
 - "AbundanceStats"
 - "AlignmentTools"
 - "Clustering"
 - "FrameBot"
 - "KmerFilter"
 - "ProbeMatch"
 - "ReadSeq"
 - "SeqFilters"
 - "SequenceMatch"
 - "classifier"
 - "constax"
 - "constax_no_inputs.sh"
 - "hmmgs"
 - "vsearch"
 - "CA.pm"
 - "cacert.pem"
 - "index-themes"
 - "fetch-extras"
 - "go.mod"
 - "go.sum"
 - "hlp-xtract.txt"
 - "index-extras"
 - "pm-collect"
versions:
 - "2.0.9--hdfd78af_0"
 - "2.0.18--pyhdfd78af_0"
 - "2.0.19--pyhdfd78af_0"
 - "2.0.20--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for constax"
config: {"url": "https://biocontainers.pro/tools/constax", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for constax", "latest": {"2.0.20--pyhdfd78af_0": "sha256:f08c23db7e07da896afc37b566af8a1658c3376f744db71fc7604b82696e7d4e"}, "tags": {"2.0.9--hdfd78af_0": "sha256:d428d99662be90f976b3352c56fe393173f51913b42b8274da8af08e77a7ac98", "2.0.18--pyhdfd78af_0": "sha256:b7090c8d1411a59a2c82058806ac74e82f971308c43d5a6bd4e986c2c29c1fb1", "2.0.19--pyhdfd78af_0": "sha256:41f80e5ac7e31cb0453a6fd7e2cb3a048977bcc74b47178152f91f3ca92974ab", "2.0.20--pyhdfd78af_0": "sha256:f08c23db7e07da896afc37b566af8a1658c3376f744db71fc7604b82696e7d4e"}, "docker": "quay.io/biocontainers/constax", "aliases": {"AbundanceStats": "/usr/local/bin/AbundanceStats", "AlignmentTools": "/usr/local/bin/AlignmentTools", "Clustering": "/usr/local/bin/Clustering", "FrameBot": "/usr/local/bin/FrameBot", "KmerFilter": "/usr/local/bin/KmerFilter", "ProbeMatch": "/usr/local/bin/ProbeMatch", "ReadSeq": "/usr/local/bin/ReadSeq", "SeqFilters": "/usr/local/bin/SeqFilters", "SequenceMatch": "/usr/local/bin/SequenceMatch", "classifier": "/usr/local/bin/classifier", "constax": "/usr/local/bin/constax", "constax_no_inputs.sh": "/usr/local/bin/constax_no_inputs.sh", "hmmgs": "/usr/local/bin/hmmgs", "vsearch": "/usr/local/bin/vsearch", "CA.pm": "/usr/local/bin/CA.pm", "cacert.pem": "/usr/local/bin/cacert.pem", "index-themes": "/usr/local/bin/index-themes", "fetch-extras": "/usr/local/bin/fetch-extras", "go.mod": "/usr/local/bin/go.mod", "go.sum": "/usr/local/bin/go.sum", "hlp-xtract.txt": "/usr/local/bin/hlp-xtract.txt", "index-extras": "/usr/local/bin/index-extras", "pm-collect": "/usr/local/bin/pm-collect"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/constax.
shpc-registry automated BioContainers addition for constax
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/constax
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/constax:2.0.20--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/constax/2.0.20--pyhdfd78af_0
$ module help quay.io/biocontainers/constax/2.0.20--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### constax-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### constax-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### constax-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### constax-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### constax-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### constax-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### AbundanceStats

```bash
$ singularity exec <container> /usr/local/bin/AbundanceStats
$ podman run --it --rm --entrypoint /usr/local/bin/AbundanceStats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/AbundanceStats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### AlignmentTools

```bash
$ singularity exec <container> /usr/local/bin/AlignmentTools
$ podman run --it --rm --entrypoint /usr/local/bin/AlignmentTools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/AlignmentTools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Clustering

```bash
$ singularity exec <container> /usr/local/bin/Clustering
$ podman run --it --rm --entrypoint /usr/local/bin/Clustering   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Clustering   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### FrameBot

```bash
$ singularity exec <container> /usr/local/bin/FrameBot
$ podman run --it --rm --entrypoint /usr/local/bin/FrameBot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FrameBot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### KmerFilter

```bash
$ singularity exec <container> /usr/local/bin/KmerFilter
$ podman run --it --rm --entrypoint /usr/local/bin/KmerFilter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/KmerFilter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ProbeMatch

```bash
$ singularity exec <container> /usr/local/bin/ProbeMatch
$ podman run --it --rm --entrypoint /usr/local/bin/ProbeMatch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ProbeMatch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ReadSeq

```bash
$ singularity exec <container> /usr/local/bin/ReadSeq
$ podman run --it --rm --entrypoint /usr/local/bin/ReadSeq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ReadSeq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SeqFilters

```bash
$ singularity exec <container> /usr/local/bin/SeqFilters
$ podman run --it --rm --entrypoint /usr/local/bin/SeqFilters   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SeqFilters   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SequenceMatch

```bash
$ singularity exec <container> /usr/local/bin/SequenceMatch
$ podman run --it --rm --entrypoint /usr/local/bin/SequenceMatch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SequenceMatch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### classifier

```bash
$ singularity exec <container> /usr/local/bin/classifier
$ podman run --it --rm --entrypoint /usr/local/bin/classifier   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/classifier   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### constax

```bash
$ singularity exec <container> /usr/local/bin/constax
$ podman run --it --rm --entrypoint /usr/local/bin/constax   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/constax   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### constax_no_inputs.sh

```bash
$ singularity exec <container> /usr/local/bin/constax_no_inputs.sh
$ podman run --it --rm --entrypoint /usr/local/bin/constax_no_inputs.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/constax_no_inputs.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmgs

```bash
$ singularity exec <container> /usr/local/bin/hmmgs
$ podman run --it --rm --entrypoint /usr/local/bin/hmmgs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmgs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vsearch

```bash
$ singularity exec <container> /usr/local/bin/vsearch
$ podman run --it --rm --entrypoint /usr/local/bin/vsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CA.pm

```bash
$ singularity exec <container> /usr/local/bin/CA.pm
$ podman run --it --rm --entrypoint /usr/local/bin/CA.pm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CA.pm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cacert.pem

```bash
$ singularity exec <container> /usr/local/bin/cacert.pem
$ podman run --it --rm --entrypoint /usr/local/bin/cacert.pem   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cacert.pem   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### index-themes

```bash
$ singularity exec <container> /usr/local/bin/index-themes
$ podman run --it --rm --entrypoint /usr/local/bin/index-themes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/index-themes   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fetch-extras

```bash
$ singularity exec <container> /usr/local/bin/fetch-extras
$ podman run --it --rm --entrypoint /usr/local/bin/fetch-extras   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fetch-extras   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### go.mod

```bash
$ singularity exec <container> /usr/local/bin/go.mod
$ podman run --it --rm --entrypoint /usr/local/bin/go.mod   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/go.mod   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### go.sum

```bash
$ singularity exec <container> /usr/local/bin/go.sum
$ podman run --it --rm --entrypoint /usr/local/bin/go.sum   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/go.sum   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hlp-xtract.txt

```bash
$ singularity exec <container> /usr/local/bin/hlp-xtract.txt
$ podman run --it --rm --entrypoint /usr/local/bin/hlp-xtract.txt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hlp-xtract.txt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### index-extras

```bash
$ singularity exec <container> /usr/local/bin/index-extras
$ podman run --it --rm --entrypoint /usr/local/bin/index-extras   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/index-extras   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pm-collect

```bash
$ singularity exec <container> /usr/local/bin/pm-collect
$ podman run --it --rm --entrypoint /usr/local/bin/pm-collect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pm-collect   -v ${PWD} -w ${PWD} <container> -c " $@"
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