---
layout: container
name:  "quay.io/biocontainers/ntm-profiler"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ntm-profiler/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/ntm-profiler/container.yaml"
updated_at: "2022-10-29 05:53:21.997941"
latest: "0.2.1--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/ntm-profiler"
aliases:
 - "add_dummy_AD.py"
 - "combine_vcf_variants.py"
 - "delly"
 - "lofreq2_indel_ovlp.py"
 - "lofreq2_vcfplot.py"
 - "ntm-profiler"
 - "rename_vcf_chrom.py"
 - "2to3-3.9"
 - "abba-baba"
 - "ace2sam"
 - "annotateBed"
 - "aserver"
 - "bFst"
 - "bamToBed"
 - "bamToFastq"
 - "bamleftalign"
 - "bc"
versions:
 - "0.2.1--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for ntm-profiler"
config: {"url": "https://biocontainers.pro/tools/ntm-profiler", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ntm-profiler", "latest": {"0.2.1--pyhdfd78af_0": "sha256:47c9986c4aab4708c3d460fb3d9b7905781be6d3e0b72771841a365de0c68788"}, "tags": {"0.2.1--pyhdfd78af_0": "sha256:47c9986c4aab4708c3d460fb3d9b7905781be6d3e0b72771841a365de0c68788"}, "docker": "quay.io/biocontainers/ntm-profiler", "aliases": {"add_dummy_AD.py": "/usr/local/bin/add_dummy_AD.py", "combine_vcf_variants.py": "/usr/local/bin/combine_vcf_variants.py", "delly": "/usr/local/bin/delly", "lofreq2_indel_ovlp.py": "/usr/local/bin/lofreq2_indel_ovlp.py", "lofreq2_vcfplot.py": "/usr/local/bin/lofreq2_vcfplot.py", "ntm-profiler": "/usr/local/bin/ntm-profiler", "rename_vcf_chrom.py": "/usr/local/bin/rename_vcf_chrom.py", "2to3-3.9": "/usr/local/bin/2to3-3.9", "abba-baba": "/usr/local/bin/abba-baba", "ace2sam": "/usr/local/bin/ace2sam", "annotateBed": "/usr/local/bin/annotateBed", "aserver": "/usr/local/bin/aserver", "bFst": "/usr/local/bin/bFst", "bamToBed": "/usr/local/bin/bamToBed", "bamToFastq": "/usr/local/bin/bamToFastq", "bamleftalign": "/usr/local/bin/bamleftalign", "bc": "/usr/local/bin/bc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ntm-profiler.
shpc-registry automated BioContainers addition for ntm-profiler
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ntm-profiler
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ntm-profiler:0.2.1--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ntm-profiler/0.2.1--pyhdfd78af_0
$ module help quay.io/biocontainers/ntm-profiler/0.2.1--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ntm-profiler-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ntm-profiler-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ntm-profiler-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ntm-profiler-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ntm-profiler-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ntm-profiler-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### add_dummy_AD.py

```bash
$ singularity exec <container> /usr/local/bin/add_dummy_AD.py
$ podman run --it --rm --entrypoint /usr/local/bin/add_dummy_AD.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/add_dummy_AD.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### combine_vcf_variants.py

```bash
$ singularity exec <container> /usr/local/bin/combine_vcf_variants.py
$ podman run --it --rm --entrypoint /usr/local/bin/combine_vcf_variants.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/combine_vcf_variants.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### delly

```bash
$ singularity exec <container> /usr/local/bin/delly
$ podman run --it --rm --entrypoint /usr/local/bin/delly   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/delly   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lofreq2_indel_ovlp.py

```bash
$ singularity exec <container> /usr/local/bin/lofreq2_indel_ovlp.py
$ podman run --it --rm --entrypoint /usr/local/bin/lofreq2_indel_ovlp.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lofreq2_indel_ovlp.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lofreq2_vcfplot.py

```bash
$ singularity exec <container> /usr/local/bin/lofreq2_vcfplot.py
$ podman run --it --rm --entrypoint /usr/local/bin/lofreq2_vcfplot.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lofreq2_vcfplot.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ntm-profiler

```bash
$ singularity exec <container> /usr/local/bin/ntm-profiler
$ podman run --it --rm --entrypoint /usr/local/bin/ntm-profiler   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ntm-profiler   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rename_vcf_chrom.py

```bash
$ singularity exec <container> /usr/local/bin/rename_vcf_chrom.py
$ podman run --it --rm --entrypoint /usr/local/bin/rename_vcf_chrom.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rename_vcf_chrom.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.9

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.9
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### abba-baba

```bash
$ singularity exec <container> /usr/local/bin/abba-baba
$ podman run --it --rm --entrypoint /usr/local/bin/abba-baba   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/abba-baba   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ace2sam

```bash
$ singularity exec <container> /usr/local/bin/ace2sam
$ podman run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annotateBed

```bash
$ singularity exec <container> /usr/local/bin/annotateBed
$ podman run --it --rm --entrypoint /usr/local/bin/annotateBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annotateBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aserver

```bash
$ singularity exec <container> /usr/local/bin/aserver
$ podman run --it --rm --entrypoint /usr/local/bin/aserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aserver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bFst

```bash
$ singularity exec <container> /usr/local/bin/bFst
$ podman run --it --rm --entrypoint /usr/local/bin/bFst   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bFst   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### bamleftalign

```bash
$ singularity exec <container> /usr/local/bin/bamleftalign
$ podman run --it --rm --entrypoint /usr/local/bin/bamleftalign   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamleftalign   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bc

```bash
$ singularity exec <container> /usr/local/bin/bc
$ podman run --it --rm --entrypoint /usr/local/bin/bc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bc   -v ${PWD} -w ${PWD} <container> -c " $@"
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