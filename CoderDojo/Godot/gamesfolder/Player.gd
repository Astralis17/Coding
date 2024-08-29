extends CharacterBody2D


const SPEED = 300.0
@export var JUMP_VELOCITY = -400.0

# players start scales
var StartScaleX
@onready var MySprite2D = $Sprite2D
@onready var MyAnimPlayer = $Sprite2D/AnimationPlayer

# Get the gravity from the project settings to be synced with RigidBody nodes.
var gravity = ProjectSettings.get_setting("physics/2d/default_gravity")

func _init():
	# sets variable to players start scale
	StartScaleX = scale.x

#handeling sprite flipping and animations
func handleFlippingAndAnimations():
	# if going right
	if velocity.x > 0:
		MySprite2D.set_flip_h(false)
		MyAnimPlayer.set_current_animation("run")
	#If going left
	elif velocity.x < 0:
		MySprite2D.set_flip_h(true)
		MyAnimPlayer.set_current_animation("run")
	#if not moving
	else:
		MyAnimPlayer.set_current_animation("idle")

func _wrapin():
	if position.y > 2000:
		position.y = -1000
	if position.x >  650:
		position.x = -638
	if position.x <  -660:
		position.x = 648
		
func _physics_process(delta):
	# Add the gravity.
	if not is_on_floor():
		velocity.y += gravity * delta

	# Handle Jump.
	if Input.is_action_just_pressed("up") and is_on_floor():
		velocity.y = JUMP_VELOCITY

	# Get the input direction and handle the movement/deceleration.
	# As good practice, you should replace UI actions with custom gameplay actions.
	var direction = Input.get_axis("left", "right")
	
	if direction:
		velocity.x = direction * SPEED
	else:
		velocity.x = move_toward(velocity.x, 0, SPEED)
	

		
	handleFlippingAndAnimations()
	move_and_slide()
	_wrapin()
