#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void name(int *count, char *fname);

int main(int argc, char *argv[])
{
    // Check for CLA
    if (argc != 2)
    {
        printf("Usage: ./recover file.raw\n");
        return 1;
    }

    // Open the file from CLA 1
    FILE *fhand = fopen(argv[1], "rb");
    if (fhand == NULL)
    {
        printf("Couldn't open %s file.\n", argv[1]);
        return 2;
    }

    // file counter and general name
    int count = 0;
    char fname[8] = "000.jpeg";
    FILE *img;

    int start = 0;

    // Read through the mem card in blocks of 512b and check whether or not it starts with the header
    uint8_t *chunks = malloc(512 * sizeof(char));
    while (fread(chunks, sizeof(chunks), 1, fhand)) 
    {
        if (chunks[0] == 0xff 
        && chunks[1] == 0xd8 
        && chunks[2] == 0xff
        && (chunks[3] & 0xf0) == 0xe0)
        {
            start = 1;
            // check for name
            name(&count, fname);
            count++;

            // Check for first image
            if (strcmp(fname, "000.jpeg") != 0)
            {
                fclose(img);
                img = fopen(fname, "wb");
                if (img == NULL)
                {
                    printf("Something went wrong\n");
                    return 3;
                }
            }
            else
            {
                img = fopen(fname, "wb");
                if (img == NULL)
                {
                    printf("Something went wrong\n");
                    return 3;
                }
            }

        }
        if (start == 1)
        {
            fwrite(chunks, sizeof(chunks), 1, img);
        }
    }

    free(chunks);
    fclose(fhand);
    return 0;
}

void name(int *count, char *fname)
{
    // Create file name
    if (*count < 10)
    {
        fname[2] = (char) (*count + 48);
    }
    else if (*count < 100)
    {
        fname[2] = (char) (*count % 10 + 48);
        fname[1] = (char) (*count / 10 % 10 + 48); 
    }
    else if (*count < 1000)
    {
        fname[2] = (char) (*count % 10 + 48);
        fname[1] = (char) (*count / 10 % 10 + 48);
        fname[0] = (char) (*count / 100 % 10 + 48);
    }

    return;
}