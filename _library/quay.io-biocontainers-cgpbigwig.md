---
layout: container
name:  "quay.io/biocontainers/cgpbigwig"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cgpbigwig/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/cgpbigwig/container.yaml"
updated_at: "2022-10-27 00:56:47.888111"
latest: "1.6.0--hbb96afb_5"
container_url: "https://biocontainers.pro/tools/cgpbigwig"
aliases:
 - "asn1Coding"
 - "asn1Decoding"
 - "asn1Parser"
 - "bam2bw"
 - "bam2bwbases"
 - "bg2bw"
 - "bwcat"
 - "bwjoin"
 - "detectExtremeDepth"
 - "p11-kit"
 - "p11tool"
 - "trust"
versions:
 - "1.6.0--hbb96afb_5"
description: "shpc-registry automated BioContainers addition for cgpbigwig"
config: {"url": "https://biocontainers.pro/tools/cgpbigwig", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for cgpbigwig", "latest": {"1.6.0--hbb96afb_5": "sha256:b1305ed5c3ffac91f0d50f9e1bfa4ab2ca985b57af67d8df5b78161e2539e734"}, "tags": {"1.6.0--hbb96afb_5": "sha256:b1305ed5c3ffac91f0d50f9e1bfa4ab2ca985b57af67d8df5b78161e2539e734"}, "docker": "quay.io/biocontainers/cgpbigwig", "aliases": {"asn1Coding": "/usr/local/bin/asn1Coding", "asn1Decoding": "/usr/local/bin/asn1Decoding", "asn1Parser": "/usr/local/bin/asn1Parser", "bam2bw": "/usr/local/bin/bam2bw", "bam2bwbases": "/usr/local/bin/bam2bwbases", "bg2bw": "/usr/local/bin/bg2bw", "bwcat": "/usr/local/bin/bwcat", "bwjoin": "/usr/local/bin/bwjoin", "detectExtremeDepth": "/usr/local/bin/detectExtremeDepth", "p11-kit": "/usr/local/bin/p11-kit", "p11tool": "/usr/local/bin/p11tool", "trust": "/usr/local/bin/trust"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cgpbigwig.
shpc-registry automated BioContainers addition for cgpbigwig
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cgpbigwig
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cgpbigwig:1.6.0--hbb96afb_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cgpbigwig/1.6.0--hbb96afb_5
$ module help quay.io/biocontainers/cgpbigwig/1.6.0--hbb96afb_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cgpbigwig-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cgpbigwig-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cgpbigwig-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cgpbigwig-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cgpbigwig-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cgpbigwig-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### asn1Coding

```bash
$ singularity exec <container> /usr/local/bin/asn1Coding
$ podman run --it --rm --entrypoint /usr/local/bin/asn1Coding   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/asn1Coding   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### asn1Decoding

```bash
$ singularity exec <container> /usr/local/bin/asn1Decoding
$ podman run --it --rm --entrypoint /usr/local/bin/asn1Decoding   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/asn1Decoding   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### asn1Parser

```bash
$ singularity exec <container> /usr/local/bin/asn1Parser
$ podman run --it --rm --entrypoint /usr/local/bin/asn1Parser   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/asn1Parser   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2bw

```bash
$ singularity exec <container> /usr/local/bin/bam2bw
$ podman run --it --rm --entrypoint /usr/local/bin/bam2bw   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2bw   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2bwbases

```bash
$ singularity exec <container> /usr/local/bin/bam2bwbases
$ podman run --it --rm --entrypoint /usr/local/bin/bam2bwbases   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2bwbases   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bg2bw

```bash
$ singularity exec <container> /usr/local/bin/bg2bw
$ podman run --it --rm --entrypoint /usr/local/bin/bg2bw   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bg2bw   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bwcat

```bash
$ singularity exec <container> /usr/local/bin/bwcat
$ podman run --it --rm --entrypoint /usr/local/bin/bwcat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwcat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bwjoin

```bash
$ singularity exec <container> /usr/local/bin/bwjoin
$ podman run --it --rm --entrypoint /usr/local/bin/bwjoin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwjoin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### detectExtremeDepth

```bash
$ singularity exec <container> /usr/local/bin/detectExtremeDepth
$ podman run --it --rm --entrypoint /usr/local/bin/detectExtremeDepth   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/detectExtremeDepth   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### p11-kit

```bash
$ singularity exec <container> /usr/local/bin/p11-kit
$ podman run --it --rm --entrypoint /usr/local/bin/p11-kit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/p11-kit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### p11tool

```bash
$ singularity exec <container> /usr/local/bin/p11tool
$ podman run --it --rm --entrypoint /usr/local/bin/p11tool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/p11tool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trust

```bash
$ singularity exec <container> /usr/local/bin/trust
$ podman run --it --rm --entrypoint /usr/local/bin/trust   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trust   -v ${PWD} -w ${PWD} <container> -c " $@"
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