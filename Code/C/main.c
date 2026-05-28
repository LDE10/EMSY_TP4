#include <stdio.h>
#include "driver/gpio.h"
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "led_strip.h"

#define BLINK_GPIO    6   // LED D1
#define BUTTON_S1     4   // Bouton S1
#define BUTTON_S2     5   // Bouton S2
#define RGB_GPIO      48  // LED RGB interne

static led_strip_handle_t led_strip;

void app_main(void) {
    // --- CONFIGURATION ---
    
    // LED D1 (Standard)
    gpio_reset_pin(BLINK_GPIO);
    gpio_set_direction(BLINK_GPIO, GPIO_MODE_OUTPUT);

    // Boutons S1 et S2
    gpio_reset_pin(BUTTON_S1);
    gpio_set_direction(BUTTON_S1, GPIO_MODE_INPUT);
    gpio_reset_pin(BUTTON_S2);
    gpio_set_direction(BUTTON_S2, GPIO_MODE_INPUT);

    // Initialisation LED RGB
    led_strip_config_t strip_config = {
        .strip_gpio_num = RGB_GPIO,
        .max_leds = 1,
    };

    // Initialisation de la configuration du périphérique RMT
    // https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-reference/peripherals/rmt.html
    led_strip_rmt_config_t rmt_config = {
        .resolution_hz = 10 * 1000 * 1000, // 10MHz
    };
    led_strip_new_rmt_device(&strip_config, &rmt_config, &led_strip);

    // Variables locales
    int led_d1_state = 0;
    int last_s1 = 1;
    int last_s2 = 1;
    typedef enum { RED, GREEN, BLUE } RGB_COLORS;
    const unsigned char colors[3][3] = {{25, 0, 0}, {0, 25, 0}, {0, 0, 25}};
    RGB_COLORS current = RED;

    led_strip_set_pixel(led_strip, 0, colors[RED][0], colors[RED][1], colors[RED][3]);
    led_strip_refresh(led_strip);

    while (1) {
        // --- BOUTON S1 (LED D1) ---
        int current_s1 = gpio_get_level(BUTTON_S1);
        if (last_s1 == 1 && current_s1 == 0) {
            vTaskDelay(50 / portTICK_PERIOD_MS);
            if (gpio_get_level(BUTTON_S1) == 0) {
                led_d1_state = !led_d1_state;
                gpio_set_level(BLINK_GPIO, led_d1_state);
            }
        }
        last_s1 = current_s1;

        // --- BOUTON S2 ---
        int current_s2 = gpio_get_level(BUTTON_S2);
        if (last_s2 == 1 && current_s2 == 0) {
            vTaskDelay(50 / portTICK_PERIOD_MS);
            if (gpio_get_level(BUTTON_S2) == 0) {
                if(current == RED || current == GREEN)
                    current++;
                else
                    current = RED;

                led_strip_set_pixel(led_strip, 0, colors[current][0], colors[current][1], colors[current][2]);
                led_strip_refresh(led_strip);
            }
        }
        last_s2 = current_s2;

        vTaskDelay(10 / portTICK_PERIOD_MS);
    }
}