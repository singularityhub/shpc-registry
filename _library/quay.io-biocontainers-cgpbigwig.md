---
layout: container
name:  "quay.io/biocontainers/cgpbigwig"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cgpbigwig/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/cgpbigwig/container.yaml"
updated_at: "2024-06-11 05:17:24.063858"
latest: "1.6.0--h8eb9e39_7"
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
 - "certtool"
 - "gnutls-cli"
 - "gnutls-cli-debug"
 - "gnutls-serv"
 - "nettle-hash"
 - "nettle-lfib-stream"
 - "nettle-pbkdf2"
 - "ocsptool"
 - "pkcs1-conv"
 - "psktool"
versions:
 - "1.6.0--hbb96afb_5"
 - "1.6.0--h87c70b1_6"
 - "1.6.0--h8eb9e39_7"
description: "shpc-registry automated BioContainers addition for cgpbigwig"
config: {"url": "https://biocontainers.pro/tools/cgpbigwig", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for cgpbigwig", "latest": {"1.6.0--h8eb9e39_7": "sha256:8e023b0d4c1d64c7c2aa0240be4696522ae71c2238bb335d33d20ada45710cae"}, "tags": {"1.6.0--hbb96afb_5": "sha256:b1305ed5c3ffac91f0d50f9e1bfa4ab2ca985b57af67d8df5b78161e2539e734", "1.6.0--h87c70b1_6": "sha256:e80c81302f23bcd627795dc469e47a5d36b634a447329677cabb54e02386bdff", "1.6.0--h8eb9e39_7": "sha256:8e023b0d4c1d64c7c2aa0240be4696522ae71c2238bb335d33d20ada45710cae"}, "docker": "quay.io/biocontainers/cgpbigwig", "aliases": {"asn1Coding": "/usr/local/bin/asn1Coding", "asn1Decoding": "/usr/local/bin/asn1Decoding", "asn1Parser": "/usr/local/bin/asn1Parser", "bam2bw": "/usr/local/bin/bam2bw", "bam2bwbases": "/usr/local/bin/bam2bwbases", "bg2bw": "/usr/local/bin/bg2bw", "bwcat": "/usr/local/bin/bwcat", "bwjoin": "/usr/local/bin/bwjoin", "detectExtremeDepth": "/usr/local/bin/detectExtremeDepth", "p11-kit": "/usr/local/bin/p11-kit", "p11tool": "/usr/local/bin/p11tool", "trust": "/usr/local/bin/trust", "certtool": "/usr/local/bin/certtool", "gnutls-cli": "/usr/local/bin/gnutls-cli", "gnutls-cli-debug": "/usr/local/bin/gnutls-cli-debug", "gnutls-serv": "/usr/local/bin/gnutls-serv", "nettle-hash": "/usr/local/bin/nettle-hash", "nettle-lfib-stream": "/usr/local/bin/nettle-lfib-stream", "nettle-pbkdf2": "/usr/local/bin/nettle-pbkdf2", "ocsptool": "/usr/local/bin/ocsptool", "pkcs1-conv": "/usr/local/bin/pkcs1-conv", "psktool": "/usr/local/bin/psktool"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cgpbigwig.
shpc-registry automated BioContainers addition for cgpbigwig
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cgpbigwig
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cgpbigwig:1.6.0--h8eb9e39_7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cgpbigwig/1.6.0--h8eb9e39_7
$ module help quay.io/biocontainers/cgpbigwig/1.6.0--h8eb9e39_7
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


#### certtool

```bash
$ singularity exec <container> /usr/local/bin/certtool
$ podman run --it --rm --entrypoint /usr/local/bin/certtool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/certtool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gnutls-cli

```bash
$ singularity exec <container> /usr/local/bin/gnutls-cli
$ podman run --it --rm --entrypoint /usr/local/bin/gnutls-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gnutls-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gnutls-cli-debug

```bash
$ singularity exec <container> /usr/local/bin/gnutls-cli-debug
$ podman run --it --rm --entrypoint /usr/local/bin/gnutls-cli-debug   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gnutls-cli-debug   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gnutls-serv

```bash
$ singularity exec <container> /usr/local/bin/gnutls-serv
$ podman run --it --rm --entrypoint /usr/local/bin/gnutls-serv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gnutls-serv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nettle-hash

```bash
$ singularity exec <container> /usr/local/bin/nettle-hash
$ podman run --it --rm --entrypoint /usr/local/bin/nettle-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nettle-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nettle-lfib-stream

```bash
$ singularity exec <container> /usr/local/bin/nettle-lfib-stream
$ podman run --it --rm --entrypoint /usr/local/bin/nettle-lfib-stream   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nettle-lfib-stream   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nettle-pbkdf2

```bash
$ singularity exec <container> /usr/local/bin/nettle-pbkdf2
$ podman run --it --rm --entrypoint /usr/local/bin/nettle-pbkdf2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nettle-pbkdf2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ocsptool

```bash
$ singularity exec <container> /usr/local/bin/ocsptool
$ podman run --it --rm --entrypoint /usr/local/bin/ocsptool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ocsptool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pkcs1-conv

```bash
$ singularity exec <container> /usr/local/bin/pkcs1-conv
$ podman run --it --rm --entrypoint /usr/local/bin/pkcs1-conv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pkcs1-conv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### psktool

```bash
$ singularity exec <container> /usr/local/bin/psktool
$ podman run --it --rm --entrypoint /usr/local/bin/psktool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/psktool   -v ${PWD} -w ${PWD} <container> -c " $@"
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