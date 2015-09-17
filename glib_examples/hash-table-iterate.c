#include <stdio.h>
#include <glib.h>

void iterator(gpointer key, gpointer val, gpointer data) {
    printf(data, *(gint*)key, val);
}

int main() {
    GHashTable * hash = g_hash_table_new(g_int_hash, g_int_equal);

    gint *k_one   = g_new(gint, 1);
    gint *k_two   = g_new(gint, 1);
    gint *k_three = g_new(gint, 1);

    *k_one   = 1;
    *k_two   = 2;
    *k_three = 3;

    g_hash_table_insert(hash, k_one, "one");
    g_hash_table_insert(hash, k_two, "four");
    g_hash_table_insert(hash, k_three, "nine");

    g_hash_table_foreach(hash, (GHFunc)iterator, "The square of %d is %s\n");
    g_hash_table_destroy(hash);

    return 0;
}
