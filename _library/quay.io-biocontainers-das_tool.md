---
layout: container
name:  "quay.io/biocontainers/das_tool"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/das_tool/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/das_tool/container.yaml"
updated_at: "2025-01-16 03:17:57.722851"
latest: "1.1.7--r44hdfd78af_1"
container_url: "https://biocontainers.pro/tools/das_tool"
aliases:
 - "Contigs2Bin_to_Fasta.sh"
 - "DAS_Tool"
 - "Fasta_to_Contig2Bin.sh"
 - "pullseq"
 - "seqdiff"
 - "erb"
 - "gem"
 - "irb"
 - "rake"
 - "rdoc"
 - "ri"
 - "ruby"
 - "funzip"
 - "unzipsfx"
 - "zipgrep"
versions:
 - "1.1.5--r41hdfd78af_0"
 - "1.1.6--r42hdfd78af_0"
 - "1.1.7--r43hdfd78af_0"
 - "1.1.7--r44hdfd78af_1"
description: "shpc-registry automated BioContainers addition for das_tool"
config: {"url": "https://biocontainers.pro/tools/das_tool", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for das_tool", "latest": {"1.1.7--r44hdfd78af_1": "sha256:8a523dd78e9b2de9a0e9548cda91e066dee6c6cb5297e5a288150f19315839c8"}, "tags": {"1.1.5--r41hdfd78af_0": "sha256:9562292c560d3d4602d917561e0efe7ea9698b6c7973112c5662f1dba996dfab", "1.1.6--r42hdfd78af_0": "sha256:db77e6420ddc5e18666251222e7617b5aac4ec0c6215ac48e16b11af9aacdd6e", "1.1.7--r43hdfd78af_0": "sha256:c7d414f509f0830880dc3eef17d009ec2eb4124b7faca9b22d0708e166baccdf", "1.1.7--r44hdfd78af_1": "sha256:8a523dd78e9b2de9a0e9548cda91e066dee6c6cb5297e5a288150f19315839c8"}, "docker": "quay.io/biocontainers/das_tool", "aliases": {"Contigs2Bin_to_Fasta.sh": "/usr/local/bin/Contigs2Bin_to_Fasta.sh", "DAS_Tool": "/usr/local/bin/DAS_Tool", "Fasta_to_Contig2Bin.sh": "/usr/local/bin/Fasta_to_Contig2Bin.sh", "pullseq": "/usr/local/bin/pullseq", "seqdiff": "/usr/local/bin/seqdiff", "erb": "/usr/local/bin/erb", "gem": "/usr/local/bin/gem", "irb": "/usr/local/bin/irb", "rake": "/usr/local/bin/rake", "rdoc": "/usr/local/bin/rdoc", "ri": "/usr/local/bin/ri", "ruby": "/usr/local/bin/ruby", "funzip": "/usr/local/bin/funzip", "unzipsfx": "/usr/local/bin/unzipsfx", "zipgrep": "/usr/local/bin/zipgrep"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/das_tool.
shpc-registry automated BioContainers addition for das_tool
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/das_tool
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/das_tool:1.1.7--r44hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/das_tool/1.1.7--r44hdfd78af_1
$ module help quay.io/biocontainers/das_tool/1.1.7--r44hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### das_tool-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### das_tool-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### das_tool-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### das_tool-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### das_tool-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### das_tool-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Contigs2Bin_to_Fasta.sh

```bash
$ singularity exec <container> /usr/local/bin/Contigs2Bin_to_Fasta.sh
$ podman run --it --rm --entrypoint /usr/local/bin/Contigs2Bin_to_Fasta.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Contigs2Bin_to_Fasta.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### DAS_Tool

```bash
$ singularity exec <container> /usr/local/bin/DAS_Tool
$ podman run --it --rm --entrypoint /usr/local/bin/DAS_Tool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/DAS_Tool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Fasta_to_Contig2Bin.sh

```bash
$ singularity exec <container> /usr/local/bin/Fasta_to_Contig2Bin.sh
$ podman run --it --rm --entrypoint /usr/local/bin/Fasta_to_Contig2Bin.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Fasta_to_Contig2Bin.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pullseq

```bash
$ singularity exec <container> /usr/local/bin/pullseq
$ podman run --it --rm --entrypoint /usr/local/bin/pullseq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pullseq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seqdiff

```bash
$ singularity exec <container> /usr/local/bin/seqdiff
$ podman run --it --rm --entrypoint /usr/local/bin/seqdiff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seqdiff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### erb

```bash
$ singularity exec <container> /usr/local/bin/erb
$ podman run --it --rm --entrypoint /usr/local/bin/erb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/erb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gem

```bash
$ singularity exec <container> /usr/local/bin/gem
$ podman run --it --rm --entrypoint /usr/local/bin/gem   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gem   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### irb

```bash
$ singularity exec <container> /usr/local/bin/irb
$ podman run --it --rm --entrypoint /usr/local/bin/irb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/irb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rake

```bash
$ singularity exec <container> /usr/local/bin/rake
$ podman run --it --rm --entrypoint /usr/local/bin/rake   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rake   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rdoc

```bash
$ singularity exec <container> /usr/local/bin/rdoc
$ podman run --it --rm --entrypoint /usr/local/bin/rdoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rdoc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ri

```bash
$ singularity exec <container> /usr/local/bin/ri
$ podman run --it --rm --entrypoint /usr/local/bin/ri   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ri   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ruby

```bash
$ singularity exec <container> /usr/local/bin/ruby
$ podman run --it --rm --entrypoint /usr/local/bin/ruby   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ruby   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### funzip

```bash
$ singularity exec <container> /usr/local/bin/funzip
$ podman run --it --rm --entrypoint /usr/local/bin/funzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/funzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unzipsfx

```bash
$ singularity exec <container> /usr/local/bin/unzipsfx
$ podman run --it --rm --entrypoint /usr/local/bin/unzipsfx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unzipsfx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zipgrep

```bash
$ singularity exec <container> /usr/local/bin/zipgrep
$ podman run --it --rm --entrypoint /usr/local/bin/zipgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zipgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
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