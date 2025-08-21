---
layout: container
name:  "quay.io/biocontainers/mity"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mity/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mity/container.yaml"
updated_at: "2025-08-21 03:27:10.780813"
latest: "2.0.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/mity"
aliases:
 - "gsort"
 - "mity"
 - "vcfanno"
 - "vcfindelproximity"
 - "vcfnullgenofields"
 - "vcfwave"
 - "split_ref_by_bai_datasize.py"
 - "sam_add_rg.pl"
 - "update_version.sh"
 - "tabix++"
 - "bamleftalign"
 - "coverage_to_regions.py"
 - "fasta_generate_regions.py"
 - "freebayes-parallel"
 - "generate_freebayes_region_scripts.sh"
 - "freebayes"
 - "abba-baba"
 - "bFst"
 - "bed2region"
 - "bgziptabix"
 - "dumpContigsFromHeader"
 - "genotypeSummary"
 - "hapLrt"
 - "iHS"
 - "meltEHH"
 - "normalize-iHS"
 - "pFst"
 - "pVst"
 - "permuteGPAT++"
 - "permuteSmooth"
 - "plotHaps"
versions:
 - "1.1.0--pyhdfd78af_0"
 - "1.2.0--pyhdfd78af_0"
 - "2.0.0--pyhdfd78af_0"
description: "singularity registry hpc automated addition for mity"
config: {"url": "https://biocontainers.pro/tools/mity", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for mity", "latest": {"2.0.0--pyhdfd78af_0": "sha256:ce96dbaad38c58be592adad26c2ca665fdb84cfeff2e4e4f1533c2a373db8606"}, "tags": {"1.1.0--pyhdfd78af_0": "sha256:4cd086cbb49cf48ff281cce13dfdf8cf0696ed15299aaed122f31be16cce37fb", "1.2.0--pyhdfd78af_0": "sha256:b83221433666f3eb4403d25be838a9e1d2897628cdb74de9b81b1f10fbc91680", "2.0.0--pyhdfd78af_0": "sha256:ce96dbaad38c58be592adad26c2ca665fdb84cfeff2e4e4f1533c2a373db8606"}, "docker": "quay.io/biocontainers/mity", "aliases": {"gsort": "/usr/local/bin/gsort", "mity": "/usr/local/bin/mity", "vcfanno": "/usr/local/bin/vcfanno", "vcfindelproximity": "/usr/local/bin/vcfindelproximity", "vcfnullgenofields": "/usr/local/bin/vcfnullgenofields", "vcfwave": "/usr/local/bin/vcfwave", "split_ref_by_bai_datasize.py": "/usr/local/bin/split_ref_by_bai_datasize.py", "sam_add_rg.pl": "/usr/local/bin/sam_add_rg.pl", "update_version.sh": "/usr/local/bin/update_version.sh", "tabix++": "/usr/local/bin/tabix++", "bamleftalign": "/usr/local/bin/bamleftalign", "coverage_to_regions.py": "/usr/local/bin/coverage_to_regions.py", "fasta_generate_regions.py": "/usr/local/bin/fasta_generate_regions.py", "freebayes-parallel": "/usr/local/bin/freebayes-parallel", "generate_freebayes_region_scripts.sh": "/usr/local/bin/generate_freebayes_region_scripts.sh", "freebayes": "/usr/local/bin/freebayes", "abba-baba": "/usr/local/bin/abba-baba", "bFst": "/usr/local/bin/bFst", "bed2region": "/usr/local/bin/bed2region", "bgziptabix": "/usr/local/bin/bgziptabix", "dumpContigsFromHeader": "/usr/local/bin/dumpContigsFromHeader", "genotypeSummary": "/usr/local/bin/genotypeSummary", "hapLrt": "/usr/local/bin/hapLrt", "iHS": "/usr/local/bin/iHS", "meltEHH": "/usr/local/bin/meltEHH", "normalize-iHS": "/usr/local/bin/normalize-iHS", "pFst": "/usr/local/bin/pFst", "pVst": "/usr/local/bin/pVst", "permuteGPAT++": "/usr/local/bin/permuteGPAT++", "permuteSmooth": "/usr/local/bin/permuteSmooth", "plotHaps": "/usr/local/bin/plotHaps"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mity.
singularity registry hpc automated addition for mity
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mity
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mity:2.0.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mity/2.0.0--pyhdfd78af_0
$ module help quay.io/biocontainers/mity/2.0.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mity-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mity-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mity-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mity-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mity-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mity-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gsort

```bash
$ singularity exec <container> /usr/local/bin/gsort
$ podman run --it --rm --entrypoint /usr/local/bin/gsort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gsort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mity

```bash
$ singularity exec <container> /usr/local/bin/mity
$ podman run --it --rm --entrypoint /usr/local/bin/mity   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mity   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcfanno

```bash
$ singularity exec <container> /usr/local/bin/vcfanno
$ podman run --it --rm --entrypoint /usr/local/bin/vcfanno   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcfanno   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcfindelproximity

```bash
$ singularity exec <container> /usr/local/bin/vcfindelproximity
$ podman run --it --rm --entrypoint /usr/local/bin/vcfindelproximity   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcfindelproximity   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcfnullgenofields

```bash
$ singularity exec <container> /usr/local/bin/vcfnullgenofields
$ podman run --it --rm --entrypoint /usr/local/bin/vcfnullgenofields   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcfnullgenofields   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcfwave

```bash
$ singularity exec <container> /usr/local/bin/vcfwave
$ podman run --it --rm --entrypoint /usr/local/bin/vcfwave   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcfwave   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### split_ref_by_bai_datasize.py

```bash
$ singularity exec <container> /usr/local/bin/split_ref_by_bai_datasize.py
$ podman run --it --rm --entrypoint /usr/local/bin/split_ref_by_bai_datasize.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/split_ref_by_bai_datasize.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sam_add_rg.pl

```bash
$ singularity exec <container> /usr/local/bin/sam_add_rg.pl
$ podman run --it --rm --entrypoint /usr/local/bin/sam_add_rg.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sam_add_rg.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### update_version.sh

```bash
$ singularity exec <container> /usr/local/bin/update_version.sh
$ podman run --it --rm --entrypoint /usr/local/bin/update_version.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/update_version.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tabix++

```bash
$ singularity exec <container> /usr/local/bin/tabix++
$ podman run --it --rm --entrypoint /usr/local/bin/tabix++   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tabix++   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamleftalign

```bash
$ singularity exec <container> /usr/local/bin/bamleftalign
$ podman run --it --rm --entrypoint /usr/local/bin/bamleftalign   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamleftalign   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### coverage_to_regions.py

```bash
$ singularity exec <container> /usr/local/bin/coverage_to_regions.py
$ podman run --it --rm --entrypoint /usr/local/bin/coverage_to_regions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coverage_to_regions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta_generate_regions.py

```bash
$ singularity exec <container> /usr/local/bin/fasta_generate_regions.py
$ podman run --it --rm --entrypoint /usr/local/bin/fasta_generate_regions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta_generate_regions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### freebayes-parallel

```bash
$ singularity exec <container> /usr/local/bin/freebayes-parallel
$ podman run --it --rm --entrypoint /usr/local/bin/freebayes-parallel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/freebayes-parallel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### generate_freebayes_region_scripts.sh

```bash
$ singularity exec <container> /usr/local/bin/generate_freebayes_region_scripts.sh
$ podman run --it --rm --entrypoint /usr/local/bin/generate_freebayes_region_scripts.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/generate_freebayes_region_scripts.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### freebayes

```bash
$ singularity exec <container> /usr/local/bin/freebayes
$ podman run --it --rm --entrypoint /usr/local/bin/freebayes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/freebayes   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### abba-baba

```bash
$ singularity exec <container> /usr/local/bin/abba-baba
$ podman run --it --rm --entrypoint /usr/local/bin/abba-baba   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/abba-baba   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bFst

```bash
$ singularity exec <container> /usr/local/bin/bFst
$ podman run --it --rm --entrypoint /usr/local/bin/bFst   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bFst   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bed2region

```bash
$ singularity exec <container> /usr/local/bin/bed2region
$ podman run --it --rm --entrypoint /usr/local/bin/bed2region   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bed2region   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bgziptabix

```bash
$ singularity exec <container> /usr/local/bin/bgziptabix
$ podman run --it --rm --entrypoint /usr/local/bin/bgziptabix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bgziptabix   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dumpContigsFromHeader

```bash
$ singularity exec <container> /usr/local/bin/dumpContigsFromHeader
$ podman run --it --rm --entrypoint /usr/local/bin/dumpContigsFromHeader   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dumpContigsFromHeader   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genotypeSummary

```bash
$ singularity exec <container> /usr/local/bin/genotypeSummary
$ podman run --it --rm --entrypoint /usr/local/bin/genotypeSummary   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genotypeSummary   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hapLrt

```bash
$ singularity exec <container> /usr/local/bin/hapLrt
$ podman run --it --rm --entrypoint /usr/local/bin/hapLrt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hapLrt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### iHS

```bash
$ singularity exec <container> /usr/local/bin/iHS
$ podman run --it --rm --entrypoint /usr/local/bin/iHS   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/iHS   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### meltEHH

```bash
$ singularity exec <container> /usr/local/bin/meltEHH
$ podman run --it --rm --entrypoint /usr/local/bin/meltEHH   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/meltEHH   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### normalize-iHS

```bash
$ singularity exec <container> /usr/local/bin/normalize-iHS
$ podman run --it --rm --entrypoint /usr/local/bin/normalize-iHS   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/normalize-iHS   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pFst

```bash
$ singularity exec <container> /usr/local/bin/pFst
$ podman run --it --rm --entrypoint /usr/local/bin/pFst   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pFst   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pVst

```bash
$ singularity exec <container> /usr/local/bin/pVst
$ podman run --it --rm --entrypoint /usr/local/bin/pVst   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pVst   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### permuteGPAT++

```bash
$ singularity exec <container> /usr/local/bin/permuteGPAT++
$ podman run --it --rm --entrypoint /usr/local/bin/permuteGPAT++   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/permuteGPAT++   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### permuteSmooth

```bash
$ singularity exec <container> /usr/local/bin/permuteSmooth
$ podman run --it --rm --entrypoint /usr/local/bin/permuteSmooth   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/permuteSmooth   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plotHaps

```bash
$ singularity exec <container> /usr/local/bin/plotHaps
$ podman run --it --rm --entrypoint /usr/local/bin/plotHaps   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plotHaps   -v ${PWD} -w ${PWD} <container> -c " $@"
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