---
layout: container
name:  "quay.io/biocontainers/pypolca"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pypolca/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pypolca/container.yaml"
updated_at: "2025-06-30 03:28:37.036435"
latest: "0.3.1--pyhdfd78af_1"
container_url: "https://biocontainers.pro/tools/pypolca"
aliases:
 - "pypolca"
 - "split_ref_by_bai_datasize.py"
 - "vcfnullgenofields"
 - "vcfwave"
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
 - "popStats"
versions:
 - "0.1.1--pyhdfd78af_0"
 - "0.2.0--pyhdfd78af_0"
 - "0.2.1--pyhdfd78af_0"
 - "0.3.1--pyhdfd78af_0"
 - "0.3.1--pyhdfd78af_1"
description: "singularity registry hpc automated addition for pypolca"
config: {"url": "https://biocontainers.pro/tools/pypolca", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for pypolca", "latest": {"0.3.1--pyhdfd78af_1": "sha256:93d320de2b313449814af69b4bdec2cf71854b306db1294fd0ad69b7be128ddc"}, "tags": {"0.1.1--pyhdfd78af_0": "sha256:bd2df98b05ced93aa1930458fbed6ba2396aa4fed08efa87ba276d33bacaec1e", "0.2.0--pyhdfd78af_0": "sha256:13d0d9c402401802d6d429c8c93e28442d1422f4d0f493a4ea8803725c6e7a3a", "0.2.1--pyhdfd78af_0": "sha256:203895a4b08f4681d959fd3a89c29dea1207838659d338b76226a81947053f0e", "0.3.1--pyhdfd78af_0": "sha256:82af8f2cba0f8c9aa8c1d221e0ac16bba423ba010ebba5e98840d08405f63519", "0.3.1--pyhdfd78af_1": "sha256:93d320de2b313449814af69b4bdec2cf71854b306db1294fd0ad69b7be128ddc"}, "docker": "quay.io/biocontainers/pypolca", "aliases": {"pypolca": "/usr/local/bin/pypolca", "split_ref_by_bai_datasize.py": "/usr/local/bin/split_ref_by_bai_datasize.py", "vcfnullgenofields": "/usr/local/bin/vcfnullgenofields", "vcfwave": "/usr/local/bin/vcfwave", "sam_add_rg.pl": "/usr/local/bin/sam_add_rg.pl", "update_version.sh": "/usr/local/bin/update_version.sh", "tabix++": "/usr/local/bin/tabix++", "bamleftalign": "/usr/local/bin/bamleftalign", "coverage_to_regions.py": "/usr/local/bin/coverage_to_regions.py", "fasta_generate_regions.py": "/usr/local/bin/fasta_generate_regions.py", "freebayes-parallel": "/usr/local/bin/freebayes-parallel", "generate_freebayes_region_scripts.sh": "/usr/local/bin/generate_freebayes_region_scripts.sh", "freebayes": "/usr/local/bin/freebayes", "abba-baba": "/usr/local/bin/abba-baba", "bFst": "/usr/local/bin/bFst", "bed2region": "/usr/local/bin/bed2region", "bgziptabix": "/usr/local/bin/bgziptabix", "dumpContigsFromHeader": "/usr/local/bin/dumpContigsFromHeader", "genotypeSummary": "/usr/local/bin/genotypeSummary", "hapLrt": "/usr/local/bin/hapLrt", "iHS": "/usr/local/bin/iHS", "meltEHH": "/usr/local/bin/meltEHH", "normalize-iHS": "/usr/local/bin/normalize-iHS", "pFst": "/usr/local/bin/pFst", "pVst": "/usr/local/bin/pVst", "permuteGPAT++": "/usr/local/bin/permuteGPAT++", "permuteSmooth": "/usr/local/bin/permuteSmooth", "plotHaps": "/usr/local/bin/plotHaps", "popStats": "/usr/local/bin/popStats"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pypolca.
singularity registry hpc automated addition for pypolca
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pypolca
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pypolca:0.3.1--pyhdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pypolca/0.3.1--pyhdfd78af_1
$ module help quay.io/biocontainers/pypolca/0.3.1--pyhdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pypolca-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pypolca-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pypolca-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pypolca-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pypolca-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pypolca-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pypolca

```bash
$ singularity exec <container> /usr/local/bin/pypolca
$ podman run --it --rm --entrypoint /usr/local/bin/pypolca   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pypolca   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### split_ref_by_bai_datasize.py

```bash
$ singularity exec <container> /usr/local/bin/split_ref_by_bai_datasize.py
$ podman run --it --rm --entrypoint /usr/local/bin/split_ref_by_bai_datasize.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/split_ref_by_bai_datasize.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### popStats

```bash
$ singularity exec <container> /usr/local/bin/popStats
$ podman run --it --rm --entrypoint /usr/local/bin/popStats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/popStats   -v ${PWD} -w ${PWD} <container> -c " $@"
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