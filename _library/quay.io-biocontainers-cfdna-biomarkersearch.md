---
layout: container
name:  "quay.io/biocontainers/cfdna-biomarkersearch"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cfdna-biomarkersearch/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/cfdna-biomarkersearch/container.yaml"
updated_at: "2026-03-23 04:44:34.961817"
latest: "0.1.3--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/cfdna-biomarkersearch"
aliases:
 - "dirmngr"
 - "dirmngr-client"
 - "gpg"
 - "gpg-agent"
 - "gpg-authcode-sign.sh"
 - "gpg-card"
 - "gpg-connect-agent"
 - "gpg-mail-tube"
 - "gpg-wks-client"
 - "gpg-wks-server"
 - "gpgconf"
 - "gpgparsemail"
 - "gpgscm"
 - "gpgsm"
 - "gpgsplit"
 - "gpgtar"
 - "gpgv"
 - "jnativescan"
 - "kbxutil"
 - "watchgnupg"
 - "plotly_get_chrome"
 - "kaleido"
 - "mathjax-path"
 - "multiqc"
 - "dotenv"
 - "funzip"
 - "unzipsfx"
 - "zipgrep"
 - "zipinfo"
 - "unzip"
 - "biom"
 - "rich-click"
 - "dumpsexp"
 - "hmac256"
 - "mpicalc"
 - "fastqc"
 - "trimmomatic"
 - "ref-cache"
 - "tar"
 - "h5fuse"
 - "idle3.14"
 - "pydoc3.14"
 - "python3.14"
 - "python3.14-config"
 - "jwebserver"
versions:
 - "0.1.1--hdfd78af_0"
 - "0.1.3--hdfd78af_0"
description: "singularity registry hpc automated addition for cfdna-biomarkersearch"
config: {"url": "https://biocontainers.pro/tools/cfdna-biomarkersearch", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for cfdna-biomarkersearch", "latest": {"0.1.3--hdfd78af_0": "sha256:5cfeb50c2c9f9c0bc5f78bfdca4cbb609225e3c6d147a03eadee668ef560e378"}, "tags": {"0.1.1--hdfd78af_0": "sha256:2bcee13b8ea7db00b28f163818566203e199ae7529c4d6b2fbf70adfb82e00f7", "0.1.3--hdfd78af_0": "sha256:5cfeb50c2c9f9c0bc5f78bfdca4cbb609225e3c6d147a03eadee668ef560e378"}, "docker": "quay.io/biocontainers/cfdna-biomarkersearch", "aliases": {"dirmngr": "/usr/local/bin/dirmngr", "dirmngr-client": "/usr/local/bin/dirmngr-client", "gpg": "/usr/local/bin/gpg", "gpg-agent": "/usr/local/bin/gpg-agent", "gpg-authcode-sign.sh": "/usr/local/bin/gpg-authcode-sign.sh", "gpg-card": "/usr/local/bin/gpg-card", "gpg-connect-agent": "/usr/local/bin/gpg-connect-agent", "gpg-mail-tube": "/usr/local/bin/gpg-mail-tube", "gpg-wks-client": "/usr/local/bin/gpg-wks-client", "gpg-wks-server": "/usr/local/bin/gpg-wks-server", "gpgconf": "/usr/local/bin/gpgconf", "gpgparsemail": "/usr/local/bin/gpgparsemail", "gpgscm": "/usr/local/bin/gpgscm", "gpgsm": "/usr/local/bin/gpgsm", "gpgsplit": "/usr/local/bin/gpgsplit", "gpgtar": "/usr/local/bin/gpgtar", "gpgv": "/usr/local/bin/gpgv", "jnativescan": "/usr/local/bin/jnativescan", "kbxutil": "/usr/local/bin/kbxutil", "watchgnupg": "/usr/local/bin/watchgnupg", "plotly_get_chrome": "/usr/local/bin/plotly_get_chrome", "kaleido": "/usr/local/bin/kaleido", "mathjax-path": "/usr/local/bin/mathjax-path", "multiqc": "/usr/local/bin/multiqc", "dotenv": "/usr/local/bin/dotenv", "funzip": "/usr/local/bin/funzip", "unzipsfx": "/usr/local/bin/unzipsfx", "zipgrep": "/usr/local/bin/zipgrep", "zipinfo": "/usr/local/bin/zipinfo", "unzip": "/usr/local/bin/unzip", "biom": "/usr/local/bin/biom", "rich-click": "/usr/local/bin/rich-click", "dumpsexp": "/usr/local/bin/dumpsexp", "hmac256": "/usr/local/bin/hmac256", "mpicalc": "/usr/local/bin/mpicalc", "fastqc": "/usr/local/bin/fastqc", "trimmomatic": "/usr/local/bin/trimmomatic", "ref-cache": "/usr/local/bin/ref-cache", "tar": "/usr/local/bin/tar", "h5fuse": "/usr/local/bin/h5fuse", "idle3.14": "/usr/local/bin/idle3.14", "pydoc3.14": "/usr/local/bin/pydoc3.14", "python3.14": "/usr/local/bin/python3.14", "python3.14-config": "/usr/local/bin/python3.14-config", "jwebserver": "/usr/local/bin/jwebserver"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cfdna-biomarkersearch.
singularity registry hpc automated addition for cfdna-biomarkersearch
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cfdna-biomarkersearch
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cfdna-biomarkersearch:0.1.3--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cfdna-biomarkersearch/0.1.3--hdfd78af_0
$ module help quay.io/biocontainers/cfdna-biomarkersearch/0.1.3--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cfdna-biomarkersearch-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cfdna-biomarkersearch-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cfdna-biomarkersearch-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cfdna-biomarkersearch-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cfdna-biomarkersearch-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cfdna-biomarkersearch-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dirmngr

```bash
$ singularity exec <container> /usr/local/bin/dirmngr
$ podman run --it --rm --entrypoint /usr/local/bin/dirmngr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dirmngr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dirmngr-client

```bash
$ singularity exec <container> /usr/local/bin/dirmngr-client
$ podman run --it --rm --entrypoint /usr/local/bin/dirmngr-client   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dirmngr-client   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gpg

```bash
$ singularity exec <container> /usr/local/bin/gpg
$ podman run --it --rm --entrypoint /usr/local/bin/gpg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gpg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gpg-agent

```bash
$ singularity exec <container> /usr/local/bin/gpg-agent
$ podman run --it --rm --entrypoint /usr/local/bin/gpg-agent   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gpg-agent   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gpg-authcode-sign.sh

```bash
$ singularity exec <container> /usr/local/bin/gpg-authcode-sign.sh
$ podman run --it --rm --entrypoint /usr/local/bin/gpg-authcode-sign.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gpg-authcode-sign.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gpg-card

```bash
$ singularity exec <container> /usr/local/bin/gpg-card
$ podman run --it --rm --entrypoint /usr/local/bin/gpg-card   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gpg-card   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gpg-connect-agent

```bash
$ singularity exec <container> /usr/local/bin/gpg-connect-agent
$ podman run --it --rm --entrypoint /usr/local/bin/gpg-connect-agent   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gpg-connect-agent   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gpg-mail-tube

```bash
$ singularity exec <container> /usr/local/bin/gpg-mail-tube
$ podman run --it --rm --entrypoint /usr/local/bin/gpg-mail-tube   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gpg-mail-tube   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gpg-wks-client

```bash
$ singularity exec <container> /usr/local/bin/gpg-wks-client
$ podman run --it --rm --entrypoint /usr/local/bin/gpg-wks-client   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gpg-wks-client   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gpg-wks-server

```bash
$ singularity exec <container> /usr/local/bin/gpg-wks-server
$ podman run --it --rm --entrypoint /usr/local/bin/gpg-wks-server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gpg-wks-server   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gpgconf

```bash
$ singularity exec <container> /usr/local/bin/gpgconf
$ podman run --it --rm --entrypoint /usr/local/bin/gpgconf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gpgconf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gpgparsemail

```bash
$ singularity exec <container> /usr/local/bin/gpgparsemail
$ podman run --it --rm --entrypoint /usr/local/bin/gpgparsemail   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gpgparsemail   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gpgscm

```bash
$ singularity exec <container> /usr/local/bin/gpgscm
$ podman run --it --rm --entrypoint /usr/local/bin/gpgscm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gpgscm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gpgsm

```bash
$ singularity exec <container> /usr/local/bin/gpgsm
$ podman run --it --rm --entrypoint /usr/local/bin/gpgsm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gpgsm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gpgsplit

```bash
$ singularity exec <container> /usr/local/bin/gpgsplit
$ podman run --it --rm --entrypoint /usr/local/bin/gpgsplit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gpgsplit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gpgtar

```bash
$ singularity exec <container> /usr/local/bin/gpgtar
$ podman run --it --rm --entrypoint /usr/local/bin/gpgtar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gpgtar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gpgv

```bash
$ singularity exec <container> /usr/local/bin/gpgv
$ podman run --it --rm --entrypoint /usr/local/bin/gpgv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gpgv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jnativescan

```bash
$ singularity exec <container> /usr/local/bin/jnativescan
$ podman run --it --rm --entrypoint /usr/local/bin/jnativescan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jnativescan   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kbxutil

```bash
$ singularity exec <container> /usr/local/bin/kbxutil
$ podman run --it --rm --entrypoint /usr/local/bin/kbxutil   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kbxutil   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### watchgnupg

```bash
$ singularity exec <container> /usr/local/bin/watchgnupg
$ podman run --it --rm --entrypoint /usr/local/bin/watchgnupg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/watchgnupg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plotly_get_chrome

```bash
$ singularity exec <container> /usr/local/bin/plotly_get_chrome
$ podman run --it --rm --entrypoint /usr/local/bin/plotly_get_chrome   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plotly_get_chrome   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kaleido

```bash
$ singularity exec <container> /usr/local/bin/kaleido
$ podman run --it --rm --entrypoint /usr/local/bin/kaleido   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kaleido   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mathjax-path

```bash
$ singularity exec <container> /usr/local/bin/mathjax-path
$ podman run --it --rm --entrypoint /usr/local/bin/mathjax-path   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mathjax-path   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### multiqc

```bash
$ singularity exec <container> /usr/local/bin/multiqc
$ podman run --it --rm --entrypoint /usr/local/bin/multiqc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/multiqc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dotenv

```bash
$ singularity exec <container> /usr/local/bin/dotenv
$ podman run --it --rm --entrypoint /usr/local/bin/dotenv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dotenv   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### zipinfo

```bash
$ singularity exec <container> /usr/local/bin/zipinfo
$ podman run --it --rm --entrypoint /usr/local/bin/zipinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zipinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unzip

```bash
$ singularity exec <container> /usr/local/bin/unzip
$ podman run --it --rm --entrypoint /usr/local/bin/unzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### biom

```bash
$ singularity exec <container> /usr/local/bin/biom
$ podman run --it --rm --entrypoint /usr/local/bin/biom   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/biom   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rich-click

```bash
$ singularity exec <container> /usr/local/bin/rich-click
$ podman run --it --rm --entrypoint /usr/local/bin/rich-click   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rich-click   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dumpsexp

```bash
$ singularity exec <container> /usr/local/bin/dumpsexp
$ podman run --it --rm --entrypoint /usr/local/bin/dumpsexp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dumpsexp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmac256

```bash
$ singularity exec <container> /usr/local/bin/hmac256
$ podman run --it --rm --entrypoint /usr/local/bin/hmac256   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmac256   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mpicalc

```bash
$ singularity exec <container> /usr/local/bin/mpicalc
$ podman run --it --rm --entrypoint /usr/local/bin/mpicalc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mpicalc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastqc

```bash
$ singularity exec <container> /usr/local/bin/fastqc
$ podman run --it --rm --entrypoint /usr/local/bin/fastqc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastqc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trimmomatic

```bash
$ singularity exec <container> /usr/local/bin/trimmomatic
$ podman run --it --rm --entrypoint /usr/local/bin/trimmomatic   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trimmomatic   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ref-cache

```bash
$ singularity exec <container> /usr/local/bin/ref-cache
$ podman run --it --rm --entrypoint /usr/local/bin/ref-cache   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ref-cache   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tar

```bash
$ singularity exec <container> /usr/local/bin/tar
$ podman run --it --rm --entrypoint /usr/local/bin/tar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5fuse

```bash
$ singularity exec <container> /usr/local/bin/h5fuse
$ podman run --it --rm --entrypoint /usr/local/bin/h5fuse   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5fuse   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### jwebserver

```bash
$ singularity exec <container> /usr/local/bin/jwebserver
$ podman run --it --rm --entrypoint /usr/local/bin/jwebserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jwebserver   -v ${PWD} -w ${PWD} <container> -c " $@"
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