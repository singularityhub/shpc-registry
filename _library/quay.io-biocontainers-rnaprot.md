---
layout: container
name:  "quay.io/biocontainers/rnaprot"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/rnaprot/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/rnaprot/container.yaml"
updated_at: "2025-01-03 03:11:47.789656"
latest: "0.5--pyhdfd78af_1"
container_url: "https://biocontainers.pro/tools/rnaprot"
aliases:
 - "RNAmultifold"
 - "bigWigAverageOverBed"
 - "gtf_extract_gene_regions.py"
 - "gtf_extract_transcript_regions.py"
 - "pyro4-check-config"
 - "pyro4-flameserver"
 - "pyro4-httpgateway"
 - "pyro4-ns"
 - "pyro4-nsc"
 - "pyro4-test-echoserver"
 - "rnaprot"
 - "torchrun"
 - "ushuffle"
 - "twoBitToFa"
 - "twoBitInfo"
 - "convert-caffe2-to-onnx"
 - "convert-onnx-to-caffe2"
 - "ninja"
 - "RNAdos"
 - "AnalyseDists"
 - "AnalyseSeqs"
 - "RNAlocmin"
 - "RNApvmin"
versions:
 - "0.5--pyhdfd78af_1"
description: "shpc-registry automated BioContainers addition for rnaprot"
config: {"url": "https://biocontainers.pro/tools/rnaprot", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for rnaprot", "latest": {"0.5--pyhdfd78af_1": "sha256:47b6bb127dcbd7524e4291b9b43689ced232eba9195274cbcc17ebc2b4235e69"}, "tags": {"0.5--pyhdfd78af_1": "sha256:47b6bb127dcbd7524e4291b9b43689ced232eba9195274cbcc17ebc2b4235e69"}, "docker": "quay.io/biocontainers/rnaprot", "aliases": {"RNAmultifold": "/usr/local/bin/RNAmultifold", "bigWigAverageOverBed": "/usr/local/bin/bigWigAverageOverBed", "gtf_extract_gene_regions.py": "/usr/local/bin/gtf_extract_gene_regions.py", "gtf_extract_transcript_regions.py": "/usr/local/bin/gtf_extract_transcript_regions.py", "pyro4-check-config": "/usr/local/bin/pyro4-check-config", "pyro4-flameserver": "/usr/local/bin/pyro4-flameserver", "pyro4-httpgateway": "/usr/local/bin/pyro4-httpgateway", "pyro4-ns": "/usr/local/bin/pyro4-ns", "pyro4-nsc": "/usr/local/bin/pyro4-nsc", "pyro4-test-echoserver": "/usr/local/bin/pyro4-test-echoserver", "rnaprot": "/usr/local/bin/rnaprot", "torchrun": "/usr/local/bin/torchrun", "ushuffle": "/usr/local/bin/ushuffle", "twoBitToFa": "/usr/local/bin/twoBitToFa", "twoBitInfo": "/usr/local/bin/twoBitInfo", "convert-caffe2-to-onnx": "/usr/local/bin/convert-caffe2-to-onnx", "convert-onnx-to-caffe2": "/usr/local/bin/convert-onnx-to-caffe2", "ninja": "/usr/local/bin/ninja", "RNAdos": "/usr/local/bin/RNAdos", "AnalyseDists": "/usr/local/bin/AnalyseDists", "AnalyseSeqs": "/usr/local/bin/AnalyseSeqs", "RNAlocmin": "/usr/local/bin/RNAlocmin", "RNApvmin": "/usr/local/bin/RNApvmin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/rnaprot.
shpc-registry automated BioContainers addition for rnaprot
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/rnaprot
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/rnaprot:0.5--pyhdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/rnaprot/0.5--pyhdfd78af_1
$ module help quay.io/biocontainers/rnaprot/0.5--pyhdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rnaprot-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rnaprot-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rnaprot-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rnaprot-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rnaprot-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rnaprot-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### RNAmultifold

```bash
$ singularity exec <container> /usr/local/bin/RNAmultifold
$ podman run --it --rm --entrypoint /usr/local/bin/RNAmultifold   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNAmultifold   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bigWigAverageOverBed

```bash
$ singularity exec <container> /usr/local/bin/bigWigAverageOverBed
$ podman run --it --rm --entrypoint /usr/local/bin/bigWigAverageOverBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bigWigAverageOverBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtf_extract_gene_regions.py

```bash
$ singularity exec <container> /usr/local/bin/gtf_extract_gene_regions.py
$ podman run --it --rm --entrypoint /usr/local/bin/gtf_extract_gene_regions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtf_extract_gene_regions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtf_extract_transcript_regions.py

```bash
$ singularity exec <container> /usr/local/bin/gtf_extract_transcript_regions.py
$ podman run --it --rm --entrypoint /usr/local/bin/gtf_extract_transcript_regions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtf_extract_transcript_regions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyro4-check-config

```bash
$ singularity exec <container> /usr/local/bin/pyro4-check-config
$ podman run --it --rm --entrypoint /usr/local/bin/pyro4-check-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyro4-check-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyro4-flameserver

```bash
$ singularity exec <container> /usr/local/bin/pyro4-flameserver
$ podman run --it --rm --entrypoint /usr/local/bin/pyro4-flameserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyro4-flameserver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyro4-httpgateway

```bash
$ singularity exec <container> /usr/local/bin/pyro4-httpgateway
$ podman run --it --rm --entrypoint /usr/local/bin/pyro4-httpgateway   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyro4-httpgateway   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyro4-ns

```bash
$ singularity exec <container> /usr/local/bin/pyro4-ns
$ podman run --it --rm --entrypoint /usr/local/bin/pyro4-ns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyro4-ns   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyro4-nsc

```bash
$ singularity exec <container> /usr/local/bin/pyro4-nsc
$ podman run --it --rm --entrypoint /usr/local/bin/pyro4-nsc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyro4-nsc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyro4-test-echoserver

```bash
$ singularity exec <container> /usr/local/bin/pyro4-test-echoserver
$ podman run --it --rm --entrypoint /usr/local/bin/pyro4-test-echoserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyro4-test-echoserver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rnaprot

```bash
$ singularity exec <container> /usr/local/bin/rnaprot
$ podman run --it --rm --entrypoint /usr/local/bin/rnaprot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rnaprot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### torchrun

```bash
$ singularity exec <container> /usr/local/bin/torchrun
$ podman run --it --rm --entrypoint /usr/local/bin/torchrun   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/torchrun   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ushuffle

```bash
$ singularity exec <container> /usr/local/bin/ushuffle
$ podman run --it --rm --entrypoint /usr/local/bin/ushuffle   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ushuffle   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### twoBitToFa

```bash
$ singularity exec <container> /usr/local/bin/twoBitToFa
$ podman run --it --rm --entrypoint /usr/local/bin/twoBitToFa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/twoBitToFa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### twoBitInfo

```bash
$ singularity exec <container> /usr/local/bin/twoBitInfo
$ podman run --it --rm --entrypoint /usr/local/bin/twoBitInfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/twoBitInfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### convert-caffe2-to-onnx

```bash
$ singularity exec <container> /usr/local/bin/convert-caffe2-to-onnx
$ podman run --it --rm --entrypoint /usr/local/bin/convert-caffe2-to-onnx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convert-caffe2-to-onnx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### convert-onnx-to-caffe2

```bash
$ singularity exec <container> /usr/local/bin/convert-onnx-to-caffe2
$ podman run --it --rm --entrypoint /usr/local/bin/convert-onnx-to-caffe2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convert-onnx-to-caffe2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ninja

```bash
$ singularity exec <container> /usr/local/bin/ninja
$ podman run --it --rm --entrypoint /usr/local/bin/ninja   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ninja   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNAdos

```bash
$ singularity exec <container> /usr/local/bin/RNAdos
$ podman run --it --rm --entrypoint /usr/local/bin/RNAdos   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNAdos   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### AnalyseDists

```bash
$ singularity exec <container> /usr/local/bin/AnalyseDists
$ podman run --it --rm --entrypoint /usr/local/bin/AnalyseDists   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/AnalyseDists   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### AnalyseSeqs

```bash
$ singularity exec <container> /usr/local/bin/AnalyseSeqs
$ podman run --it --rm --entrypoint /usr/local/bin/AnalyseSeqs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/AnalyseSeqs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNAlocmin

```bash
$ singularity exec <container> /usr/local/bin/RNAlocmin
$ podman run --it --rm --entrypoint /usr/local/bin/RNAlocmin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNAlocmin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNApvmin

```bash
$ singularity exec <container> /usr/local/bin/RNApvmin
$ podman run --it --rm --entrypoint /usr/local/bin/RNApvmin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNApvmin   -v ${PWD} -w ${PWD} <container> -c " $@"
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