---
layout: container
name:  "quay.io/biocontainers/barcodeforge"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/barcodeforge/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/barcodeforge/container.yaml"
updated_at: "2025-08-31 03:12:25.005640"
latest: "1.1.1--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/barcodeforge"
aliases:
 - "augur"
 - "barcodeforge"
 - "bottle.py"
 - "dsdp5"
 - "ete4"
 - "faToVcf"
 - "fido2-assert"
 - "fido2-cred"
 - "fido2-token"
 - "matOptimize"
 - "matUtils"
 - "ripples"
 - "scp"
 - "sftp"
 - "ssh"
 - "ssh-add"
 - "ssh-agent"
 - "ssh-keygen"
 - "ssh-keyscan"
 - "sshd"
 - "stringify"
 - "sumlabels"
 - "sumtrees"
 - "treetime"
 - "usher"
 - "vcftools"
 - "fill-aa"
 - "fill-an-ac"
 - "fill-fs"
 - "fill-ref-md5"
 - "vcf-annotate"
 - "vcf-compare"
 - "vcf-concat"
 - "vcf-consensus"
 - "vcf-contrast"
 - "vcf-convert"
 - "vcf-fix-newlines"
 - "vcf-fix-ploidy"
 - "vcf-indel-stats"
 - "vcf-isec"
 - "vcf-merge"
 - "vcf-phased-join"
 - "vcf-query"
 - "vcf-shuffle-cols"
 - "vcf-sort"
 - "vcf-stats"
 - "vcf-subset"
 - "vcf-to-tab"
 - "vcf-tstv"
 - "vcf-validator"
 - "gawk-5.3.1"
versions:
 - "1.0.0--pyhdfd78af_0"
 - "1.1.1--pyhdfd78af_0"
description: "singularity registry hpc automated addition for barcodeforge"
config: {"url": "https://biocontainers.pro/tools/barcodeforge", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for barcodeforge", "latest": {"1.1.1--pyhdfd78af_0": "sha256:fb0fd0fbe7e53a4fdb6e8a46d1ca0423123b4e5c0d77d90e9d1a36809332e6e3"}, "tags": {"1.0.0--pyhdfd78af_0": "sha256:8968127dbd4f8d45f9f676bf1749225e73c9c80261d13079ff3872341803a982", "1.1.1--pyhdfd78af_0": "sha256:fb0fd0fbe7e53a4fdb6e8a46d1ca0423123b4e5c0d77d90e9d1a36809332e6e3"}, "docker": "quay.io/biocontainers/barcodeforge", "aliases": {"augur": "/usr/local/bin/augur", "barcodeforge": "/usr/local/bin/barcodeforge", "bottle.py": "/usr/local/bin/bottle.py", "dsdp5": "/usr/local/bin/dsdp5", "ete4": "/usr/local/bin/ete4", "faToVcf": "/usr/local/bin/faToVcf", "fido2-assert": "/usr/local/bin/fido2-assert", "fido2-cred": "/usr/local/bin/fido2-cred", "fido2-token": "/usr/local/bin/fido2-token", "matOptimize": "/usr/local/bin/matOptimize", "matUtils": "/usr/local/bin/matUtils", "ripples": "/usr/local/bin/ripples", "scp": "/usr/local/bin/scp", "sftp": "/usr/local/bin/sftp", "ssh": "/usr/local/bin/ssh", "ssh-add": "/usr/local/bin/ssh-add", "ssh-agent": "/usr/local/bin/ssh-agent", "ssh-keygen": "/usr/local/bin/ssh-keygen", "ssh-keyscan": "/usr/local/bin/ssh-keyscan", "sshd": "/usr/local/bin/sshd", "stringify": "/usr/local/bin/stringify", "sumlabels": "/usr/local/bin/sumlabels", "sumtrees": "/usr/local/bin/sumtrees", "treetime": "/usr/local/bin/treetime", "usher": "/usr/local/bin/usher", "vcftools": "/usr/local/bin/vcftools", "fill-aa": "/usr/local/bin/fill-aa", "fill-an-ac": "/usr/local/bin/fill-an-ac", "fill-fs": "/usr/local/bin/fill-fs", "fill-ref-md5": "/usr/local/bin/fill-ref-md5", "vcf-annotate": "/usr/local/bin/vcf-annotate", "vcf-compare": "/usr/local/bin/vcf-compare", "vcf-concat": "/usr/local/bin/vcf-concat", "vcf-consensus": "/usr/local/bin/vcf-consensus", "vcf-contrast": "/usr/local/bin/vcf-contrast", "vcf-convert": "/usr/local/bin/vcf-convert", "vcf-fix-newlines": "/usr/local/bin/vcf-fix-newlines", "vcf-fix-ploidy": "/usr/local/bin/vcf-fix-ploidy", "vcf-indel-stats": "/usr/local/bin/vcf-indel-stats", "vcf-isec": "/usr/local/bin/vcf-isec", "vcf-merge": "/usr/local/bin/vcf-merge", "vcf-phased-join": "/usr/local/bin/vcf-phased-join", "vcf-query": "/usr/local/bin/vcf-query", "vcf-shuffle-cols": "/usr/local/bin/vcf-shuffle-cols", "vcf-sort": "/usr/local/bin/vcf-sort", "vcf-stats": "/usr/local/bin/vcf-stats", "vcf-subset": "/usr/local/bin/vcf-subset", "vcf-to-tab": "/usr/local/bin/vcf-to-tab", "vcf-tstv": "/usr/local/bin/vcf-tstv", "vcf-validator": "/usr/local/bin/vcf-validator", "gawk-5.3.1": "/usr/local/bin/gawk-5.3.1"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/barcodeforge.
singularity registry hpc automated addition for barcodeforge
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/barcodeforge
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/barcodeforge:1.1.1--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/barcodeforge/1.1.1--pyhdfd78af_0
$ module help quay.io/biocontainers/barcodeforge/1.1.1--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### barcodeforge-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### barcodeforge-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### barcodeforge-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### barcodeforge-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### barcodeforge-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### barcodeforge-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### augur

```bash
$ singularity exec <container> /usr/local/bin/augur
$ podman run --it --rm --entrypoint /usr/local/bin/augur   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/augur   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### barcodeforge

```bash
$ singularity exec <container> /usr/local/bin/barcodeforge
$ podman run --it --rm --entrypoint /usr/local/bin/barcodeforge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/barcodeforge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bottle.py

```bash
$ singularity exec <container> /usr/local/bin/bottle.py
$ podman run --it --rm --entrypoint /usr/local/bin/bottle.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bottle.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dsdp5

```bash
$ singularity exec <container> /usr/local/bin/dsdp5
$ podman run --it --rm --entrypoint /usr/local/bin/dsdp5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dsdp5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ete4

```bash
$ singularity exec <container> /usr/local/bin/ete4
$ podman run --it --rm --entrypoint /usr/local/bin/ete4   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ete4   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### faToVcf

```bash
$ singularity exec <container> /usr/local/bin/faToVcf
$ podman run --it --rm --entrypoint /usr/local/bin/faToVcf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/faToVcf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fido2-assert

```bash
$ singularity exec <container> /usr/local/bin/fido2-assert
$ podman run --it --rm --entrypoint /usr/local/bin/fido2-assert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fido2-assert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fido2-cred

```bash
$ singularity exec <container> /usr/local/bin/fido2-cred
$ podman run --it --rm --entrypoint /usr/local/bin/fido2-cred   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fido2-cred   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fido2-token

```bash
$ singularity exec <container> /usr/local/bin/fido2-token
$ podman run --it --rm --entrypoint /usr/local/bin/fido2-token   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fido2-token   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### matOptimize

```bash
$ singularity exec <container> /usr/local/bin/matOptimize
$ podman run --it --rm --entrypoint /usr/local/bin/matOptimize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/matOptimize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### matUtils

```bash
$ singularity exec <container> /usr/local/bin/matUtils
$ podman run --it --rm --entrypoint /usr/local/bin/matUtils   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/matUtils   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ripples

```bash
$ singularity exec <container> /usr/local/bin/ripples
$ podman run --it --rm --entrypoint /usr/local/bin/ripples   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ripples   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scp

```bash
$ singularity exec <container> /usr/local/bin/scp
$ podman run --it --rm --entrypoint /usr/local/bin/scp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sftp

```bash
$ singularity exec <container> /usr/local/bin/sftp
$ podman run --it --rm --entrypoint /usr/local/bin/sftp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sftp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ssh

```bash
$ singularity exec <container> /usr/local/bin/ssh
$ podman run --it --rm --entrypoint /usr/local/bin/ssh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ssh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ssh-add

```bash
$ singularity exec <container> /usr/local/bin/ssh-add
$ podman run --it --rm --entrypoint /usr/local/bin/ssh-add   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ssh-add   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ssh-agent

```bash
$ singularity exec <container> /usr/local/bin/ssh-agent
$ podman run --it --rm --entrypoint /usr/local/bin/ssh-agent   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ssh-agent   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ssh-keygen

```bash
$ singularity exec <container> /usr/local/bin/ssh-keygen
$ podman run --it --rm --entrypoint /usr/local/bin/ssh-keygen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ssh-keygen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ssh-keyscan

```bash
$ singularity exec <container> /usr/local/bin/ssh-keyscan
$ podman run --it --rm --entrypoint /usr/local/bin/ssh-keyscan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ssh-keyscan   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sshd

```bash
$ singularity exec <container> /usr/local/bin/sshd
$ podman run --it --rm --entrypoint /usr/local/bin/sshd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sshd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### stringify

```bash
$ singularity exec <container> /usr/local/bin/stringify
$ podman run --it --rm --entrypoint /usr/local/bin/stringify   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/stringify   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sumlabels

```bash
$ singularity exec <container> /usr/local/bin/sumlabels
$ podman run --it --rm --entrypoint /usr/local/bin/sumlabels   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sumlabels   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sumtrees

```bash
$ singularity exec <container> /usr/local/bin/sumtrees
$ podman run --it --rm --entrypoint /usr/local/bin/sumtrees   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sumtrees   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### treetime

```bash
$ singularity exec <container> /usr/local/bin/treetime
$ podman run --it --rm --entrypoint /usr/local/bin/treetime   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/treetime   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### usher

```bash
$ singularity exec <container> /usr/local/bin/usher
$ podman run --it --rm --entrypoint /usr/local/bin/usher   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/usher   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcftools

```bash
$ singularity exec <container> /usr/local/bin/vcftools
$ podman run --it --rm --entrypoint /usr/local/bin/vcftools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcftools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fill-aa

```bash
$ singularity exec <container> /usr/local/bin/fill-aa
$ podman run --it --rm --entrypoint /usr/local/bin/fill-aa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fill-aa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fill-an-ac

```bash
$ singularity exec <container> /usr/local/bin/fill-an-ac
$ podman run --it --rm --entrypoint /usr/local/bin/fill-an-ac   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fill-an-ac   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fill-fs

```bash
$ singularity exec <container> /usr/local/bin/fill-fs
$ podman run --it --rm --entrypoint /usr/local/bin/fill-fs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fill-fs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fill-ref-md5

```bash
$ singularity exec <container> /usr/local/bin/fill-ref-md5
$ podman run --it --rm --entrypoint /usr/local/bin/fill-ref-md5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fill-ref-md5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf-annotate

```bash
$ singularity exec <container> /usr/local/bin/vcf-annotate
$ podman run --it --rm --entrypoint /usr/local/bin/vcf-annotate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf-annotate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf-compare

```bash
$ singularity exec <container> /usr/local/bin/vcf-compare
$ podman run --it --rm --entrypoint /usr/local/bin/vcf-compare   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf-compare   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf-concat

```bash
$ singularity exec <container> /usr/local/bin/vcf-concat
$ podman run --it --rm --entrypoint /usr/local/bin/vcf-concat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf-concat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf-consensus

```bash
$ singularity exec <container> /usr/local/bin/vcf-consensus
$ podman run --it --rm --entrypoint /usr/local/bin/vcf-consensus   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf-consensus   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf-contrast

```bash
$ singularity exec <container> /usr/local/bin/vcf-contrast
$ podman run --it --rm --entrypoint /usr/local/bin/vcf-contrast   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf-contrast   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf-convert

```bash
$ singularity exec <container> /usr/local/bin/vcf-convert
$ podman run --it --rm --entrypoint /usr/local/bin/vcf-convert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf-convert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf-fix-newlines

```bash
$ singularity exec <container> /usr/local/bin/vcf-fix-newlines
$ podman run --it --rm --entrypoint /usr/local/bin/vcf-fix-newlines   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf-fix-newlines   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf-fix-ploidy

```bash
$ singularity exec <container> /usr/local/bin/vcf-fix-ploidy
$ podman run --it --rm --entrypoint /usr/local/bin/vcf-fix-ploidy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf-fix-ploidy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf-indel-stats

```bash
$ singularity exec <container> /usr/local/bin/vcf-indel-stats
$ podman run --it --rm --entrypoint /usr/local/bin/vcf-indel-stats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf-indel-stats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf-isec

```bash
$ singularity exec <container> /usr/local/bin/vcf-isec
$ podman run --it --rm --entrypoint /usr/local/bin/vcf-isec   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf-isec   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf-merge

```bash
$ singularity exec <container> /usr/local/bin/vcf-merge
$ podman run --it --rm --entrypoint /usr/local/bin/vcf-merge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf-merge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf-phased-join

```bash
$ singularity exec <container> /usr/local/bin/vcf-phased-join
$ podman run --it --rm --entrypoint /usr/local/bin/vcf-phased-join   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf-phased-join   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf-query

```bash
$ singularity exec <container> /usr/local/bin/vcf-query
$ podman run --it --rm --entrypoint /usr/local/bin/vcf-query   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf-query   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf-shuffle-cols

```bash
$ singularity exec <container> /usr/local/bin/vcf-shuffle-cols
$ podman run --it --rm --entrypoint /usr/local/bin/vcf-shuffle-cols   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf-shuffle-cols   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf-sort

```bash
$ singularity exec <container> /usr/local/bin/vcf-sort
$ podman run --it --rm --entrypoint /usr/local/bin/vcf-sort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf-sort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf-stats

```bash
$ singularity exec <container> /usr/local/bin/vcf-stats
$ podman run --it --rm --entrypoint /usr/local/bin/vcf-stats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf-stats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf-subset

```bash
$ singularity exec <container> /usr/local/bin/vcf-subset
$ podman run --it --rm --entrypoint /usr/local/bin/vcf-subset   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf-subset   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf-to-tab

```bash
$ singularity exec <container> /usr/local/bin/vcf-to-tab
$ podman run --it --rm --entrypoint /usr/local/bin/vcf-to-tab   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf-to-tab   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf-tstv

```bash
$ singularity exec <container> /usr/local/bin/vcf-tstv
$ podman run --it --rm --entrypoint /usr/local/bin/vcf-tstv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf-tstv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf-validator

```bash
$ singularity exec <container> /usr/local/bin/vcf-validator
$ podman run --it --rm --entrypoint /usr/local/bin/vcf-validator   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf-validator   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawk-5.3.1

```bash
$ singularity exec <container> /usr/local/bin/gawk-5.3.1
$ podman run --it --rm --entrypoint /usr/local/bin/gawk-5.3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawk-5.3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
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